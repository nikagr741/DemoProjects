🚀 Distributed Task Queue with gRPC, Redis, and PostgreSQL
This project demonstrates a high-performance Asynchronous Task Pattern. It solves the problem of "blocking" APIs by offloading heavy computational work to background workers while maintaining data integrity using a relational database.

🏗️ System Architecture
The system is composed of four decoupled layers:

gRPC Producer (Server): Receives requests and immediately returns a tracking ID.

Redis (Message Broker): Acts as the high-speed queue for pending tasks.

Celery Worker (Consumer): Picks up tasks from Redis and performs the "heavy lifting."

PostgreSQL (State Store): The source of truth for task statuses (Pending, Processing, Completed).

🛠️ Tech Stack
Language: Python 3.x

Communication: gRPC (Protocol Buffers)

Task Management: Celery

Broker: Redis

Database: PostgreSQL

Infrastructure: Docker & Docker Compose

🚀 Quick Start
1. Spin up Infrastructure
Use Docker Compose to start the database and the message broker:

Bash
docker-compose up -d
2. Initialize the Database
Enter the Postgres container and create the tasks table:

Bash
docker exec -it postgres_db psql -U nikhil_user -d task_db
# Run the SQL found in schema.sql
3. Start the Background Worker
In a new terminal, launch the Celery worker:

Bash
celery -A worker worker --loglevel=info -P solo
4. Run the gRPC Server & Client
Bash
python server.py
python client.py
🧠 Key Features & Learning Outcomes
Non-Blocking API: The gRPC server remains responsive even while processing 10+ second tasks.

Infrastructure as Code: Every dependency is containerized for "one-click" setup.

Data Persistence: Even if the worker crashes, the task state is safely recorded in Postgres.

Decoupling: The Server and Worker are completely separate processes, allowing them to scale independently.