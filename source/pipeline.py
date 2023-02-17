
# import statements



class pipeline():
    """
    Object for importing and cleaning electrolarynx video feeds prior to prediction
    """
    def __init__(self):
        #TODO: Implement pipeline base object
        return None

    def import_videos(self, source_url):
        """
        Method for importing new videos given a source_url or similar.

        :return:
            - imported videos (object? tbd)
        """
        #TODO: implement pipeline.import_videos()
        return None

    def get_audio(self):
        """
        Method for pulling audio from imported video viles

        :return:
            - matrix of audio files
        """
        #TODO: implement pipeline.get_audio()
        return None

    def feature_engineering(self):
        """
        Method for cleaning audio files into data we can run model.predict() on.

        :return:
            - matrix of features
        """
        #TODO: implement pipeline.feature_engineering()
        return None

    