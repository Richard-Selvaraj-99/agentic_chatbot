from configparser import ConfigParser

class Config:
    def __init__(self,config_file=".src\langraphagenticai\ui\uiconfigfile.ini"):
        self.config=ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        return self.cofig["DEFAULT"].get["LLM_OPTIONS"].split(", ")
    
    def get_usecae_options(self):
        return self.cofig["DEFAULT"].get["USECASE_OPTIONS"].split(", ")
    
    def get_groq_model_options(self):
        return self.cofig["DEFAULT"].get["GROQ_MODEL_OPTIONS"].split(", ")
    
    def get_page_title(self):
        return self.cofig["DEFAULT"].get["PAGE_TITLE"]