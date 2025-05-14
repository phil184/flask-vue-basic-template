setup:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && cd frontend && npm install && cd ..
	
run-backend:
	source venv/bin/activate && flask run

run-frontend:
	cd frontend && npm run dev

clean:
	rm -rf venv frontend/node_modules