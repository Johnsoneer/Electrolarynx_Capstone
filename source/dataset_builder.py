import os
from boxsdk import OAuth2, Client
import pandas as pd
import shutil


class datasetBuilder():
    def __init__(self, shared_folder_url = "https://virginia.app.box.com/s/02c54h85czvwlfxsg9lu5n4zfatdmwqd"):
        self.shared_folder_url = shared_folder_url
        
    def set_env_variables(self):
        # You'll need a Box developer token to pull our data.
        # Generate one at this URL:https://virginia.app.box.com/developers/console/app/1957103/configuration 
        
        dev_url = 'https://virginia.app.box.com/developers/console'
        print("*** You'll need API credentials to move forward ***")
        print("create credentials in the box developers console: {}".format(dev_url))
        client_id = input("Please enter your CLIENT_ID: ")
        client_secret = input("Please enter your CLIENT_SECRET: ")
        developer_token = input("Please enter your DEVELOPER_TOKEN: ")

        os.environ['BOX_CLIENT_ID'] = client_id
        os.environ['BOX_CLIENT_SECRET'] = client_secret
        os.environ['BOX_DEVELOPER_TOKEN'] = developer_token

    def connect_to_box(self):
        '''
        Given credentials in our python environment, create a connection 
        client to the API endpoint.
        '''
        print("*** Authenticating connection to Box API ***")
        try: 
            client_id = os.environ['BOX_CLIENT_ID'] 
            client_secret = os.environ['BOX_CLIENT_SECRET'] 
            developer_token = os.environ['BOX_DEVELOPER_TOKEN'] 
        except:
            self.set_env_variables()
            client_id = os.environ['BOX_CLIENT_ID'] 
            client_secret = os.environ['BOX_CLIENT_SECRET'] 
            developer_token = os.environ['BOX_DEVELOPER_TOKEN'] 

        auth = OAuth2(
            client_id=client_id,
            client_secret=client_secret,
            access_token=developer_token,
        )
        self.client = Client(auth)


    def check_dataset_exists(self, directory = 'data/'):
        '''
        Check to see if the dataset is already here and prompt the user for overwrite.
        '''
        if os.path.exists(directory):
            response = input("*** data directory already present. Overwrite current dataset?(Y/n)")
            if response == "Y":
               # Deleting an non-empty folder
                shutil.rmtree(directory, ignore_errors=True)
                return False
            else:
                return True
        else:
            return False 

    def download_dataset(self):
        """
        Given a url of a shared folder link to our dataset, check to see
        if we have the dataset in this directory. If not, import the dataset
        and save to our data directory.
        """

        #check for dataset in current repository
        os.chdir("..")

        if self.check_dataset_exists():
            return None
        else:
            os.mkdir("data/", 0o777)
            os.chdir("data/")

        # build api connection object
        box_obj = self.client.get_shared_item(self.shared_folder_url, password='letmein')

        # collect metadata
        metadata = self.collect_metadata(box_obj)
        metadata.to_csv("metadata.csv")

        # download dataset
        self.recursive_download(box_obj, "data")



    def collect_metadata(self, obj):
        """
        Given a connection object to the Box API, collect the relavant 
        names/ids/directory names of each file
        """
        files = []

        def populate_files(node, parent):
            """
            Recursively moves through Box tree structure and builds a 
            list of files and their labels
            """
            if node.type == "folder":
                for item in node.get_items():
                    populate_files(item, parent+"/"+node.name)
            elif node.type == "file":
                name = node.name
                id = node.id
                parent = parent
                files.append({"name":name, "id":id, "directory":parent})

        populate_files(obj, "root")  
        return pd.DataFrame(files)

    def recursive_download(self, node, parent):
        '''
        Given a root directory from the API, download each directory
        and each file in said directory
        '''
        if node.type == "folder":
            os.mkdir(f"{node.name}/", 0o777)
            os.chdir(f"{node.name}/")
            for item in node.get_items():
                self.recursive_download(item, node.name)
            os.chdir("..")
        elif node.type == "file":
            filename = node.name
            with open(filename, 'wb') as open_file:
                node.download_to(open_file)
                open_file.close()
            return None
        else:
            return None
        
# Run the above to build the dataset
if __name__=="__main__":
    folder = input("input box folder URL: ")
    builder = datasetBuilder(shared_folder_url = folder)
    builder.connect_to_box()
    builder.download_dataset()