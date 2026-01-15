# Makefile
.PHONY: start stop clean restart check-supabase eval-collect eval-run logs

# Check if Supabase is running
check-supabase:
	@echo "Checking Supabase..."
	@npx supabase start
	@npx supabase status > /dev/null 2>&1 && echo "✓ Supabase is running" || (echo "✗ Supabase failed to start" && exit 1)

PROJECT_NAME=mindbook

start: check-supabase
	@echo "Starting Docker containers..."
	@echo "Building Docker images..."
	docker-compose -p $(PROJECT_NAME) build
	@echo "Starting containers..."
	docker-compose -p $(PROJECT_NAME) up -d

# Stop all containers
stop:
	@echo "Stopping Docker containers..."
	docker-compose -p $(PROJECT_NAME) down

# Clean everything (containers, images, volumes)
clean:
	@echo "Cleaning all Docker resources..."
	docker-compose -p $(PROJECT_NAME) down -v --rmi all --remove-orphans

# Restart all containers
restart: stop start

# View API server logs
logs-api:
	@echo "Showing API server logs (Ctrl+C to exit)..."
	docker-compose -p $(PROJECT_NAME) logs -f api

# View API server logs
logs-redis:
	@echo "Showing Redis server logs (Ctrl+C to exit)..."
	docker-compose -p $(PROJECT_NAME) logs -f redis

# View Worker logs
logs-worker:
	@echo "Showing Worker logs (Ctrl+C to exit)..."
	docker-compose -p $(PROJECT_NAME) logs -f worker



start-containers:
	@echo "Starting Docker containers..."
	docker-compose up -d