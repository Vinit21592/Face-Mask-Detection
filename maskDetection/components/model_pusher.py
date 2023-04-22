import sys
from maskDetection.configuration.s3_operations import S3Operation
from maskDetection.entity.artifact_entity import (ModelPusherArtifact,
                                                  ModelTrainerArtifact)
from maskDetection.entity.config_entity import ModelPusherConfig
from maskDetection.logger import logging
from maskDetection.exception import MaskException


class ModelPusher:
    def __init__(self,model_pusher_config:ModelPusherConfig,
                 model_trainer_artifact:ModelTrainerArtifact,
                 s3:S3Operation) -> None:
        try:
            self.model_pusher_config = model_pusher_config
            self.model_trainer_artifact = model_trainer_artifact
            self.s3 = s3
        except Exception as e:
            raise MaskException(e,sys)
        

    def initiate_model_pusher(self)->ModelPusherArtifact:

        """
        Method Name :   initiate_model_pusher
        Description :   This method initiates model pusher. 
        Output      :   Model pusher artifact 
        """
        logging.info("Entered initiate_model_pusher method of Modelpusher class")
        try:
            # Uploading the best model to s3 bucket
            self.s3.upload_file(
                self.model_trainer_artifact.trained_model_file_path,
                self.model_pusher_config.S3_MODEL_KEY_PATH,
                self.model_pusher_config.BUCKET_NAME,
                remove=False,
            )
            logging.info("Uploaded best model to s3 bucket")
            logging.info("Exited initiate_model_pusher method of ModelTrainer class")

            # Saving the model pusher artifacts
            model_pusher_artifact = ModelPusherArtifact(
                bucket_name=self.model_pusher_config.BUCKET_NAME,
                s3_model_path=self.model_pusher_config.S3_MODEL_KEY_PATH,
            )

            return model_pusher_artifact
        
        except Exception as e:
            raise Exception(e,sys) from e