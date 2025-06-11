mkdir -p backend/app/{api,models,crud,schemas,services,core}   
touch backend/main.py backend/requirements.txt   

npm create vite@latest frontend -- --template react-ts   
cd frontend 

npm install react-router-dom 
npm install axios

npm install && cd ..   

