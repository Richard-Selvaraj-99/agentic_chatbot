<details>
---
title: Agentic AI Web Chatbot
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: streamlit
python_version: "3.10"
app_file: app.py
pinned: false
---
</details>
# working Hugging_face link [text](https://huggingface.co/spaces/Richard9905/agentic_ai_web_chatbot)
### workflows proof
[![Production CI/CD Pipeline](https://github.com/Richard-Selvaraj-99/agentic_chatbot/actions/workflows/deploy.yml/badge.svg?event=deployment_status)](https://github.com/Richard-Selvaraj-99/agentic_chatbot/actions/workflows/deploy.yml)
[![Production CI/CD Pipeline](https://github.com/Richard-Selvaraj-99/agentic_chatbot/actions/workflows/deploy.yml/badge.svg)](https://github.com/Richard-Selvaraj-99/agentic_chatbot/actions/workflows/deploy.yml)
[![CI/CD Pipeline](https://github.com/Richard-Selvaraj-99/Agentic_AI_with_github_CI-CD_and_Huggingface_deployment/actions/workflows/deploy.yml/badge.svg)](https://github.com/Richard-Selvaraj-99/Agentic_AI_with_github_CI-CD_and_Huggingface_deployment/actions/workflows/deploy.yml)

#STEP BY STEP PROCESS OF HOW TO RE-CREATE THIS PROJECT

##REQUIREMENTS
###1.LIBRARIES AS WRITTEN IN  requirements.txt
###2.create environment
  -conda create -p  ./venv python ==3.13 -y
  -pip install -r requirements.txt
  -conda activate ./venv
###3.create git repo using git CLI
  -gh repo create
  -create rep name
  -select public or private (your choice)
  -create gitignore for python (type necessary files and folders to be avoided)
###4. then git clone (https://github.com/Richard-Selvaraj-99/Agentic_AI_with_github_CI-CD_and_Huggingface_deployment/tree/main)
###6.In the terminal run (pytest) for locally testing the envrionment varaibles
###7.then create a hf link edit the deploy.yml with the right link 
###8.In repo secrets upload HF_TOEKN , DOCKER_USERNAME, DOCKER_PASSWORD
###9.once the action workflow works go to the hf repo space link and select: 
   --basic chat bot for non-agentic workflow
   --chatbot with web for agentic workflow
