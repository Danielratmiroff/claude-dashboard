# Claude Code Metrics Dashboard

Docker Compose stack for visualizing Claude Code metrics using Grafana.

## Quick Start

1. Start the stack:
   ```bash
   cd docker
   docker compose up -d
   ```

2. Configure Claude Code to export metrics. Add to `~/.claude/settings.json`:
   ```json
   {
     "otel": {
       "enabled": true,
       "endpoint": "http://localhost:4317",
       "protocol": "grpc",
       "serviceName": "claude-code"
     }
   }
   ```

3. Open Grafana at http://localhost:3000

## Services

| Service | Port | Description |
|---------|------|-------------|
| OTel Collector | 4317 | Receives metrics from Claude Code |
| Prometheus | 9090 | Stores metrics with 15-day retention |
| Grafana | 3000 | Dashboard UI (anonymous access) |

## Commands

```bash
# Start
docker compose up -d

# Stop
docker compose down

# View logs
docker compose logs -f

# Reset data (removes metrics history)
docker compose down -v
```

## Metrics Tracked

- Token usage (input, output, cache read, cache creation)
- API cost by model
- Active time (CLI vs user)
- Commits made
- Lines of code
