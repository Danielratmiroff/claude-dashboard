# Claude Code Metrics Dashboard

Grafana dashboard for visualizing Claude Code usage metrics.

## Quick Start

1. Start the stack:
   ```bash
   docker compose up -d
   ```

2. Add to `~/.claude/settings.json`:
   ```json
   {
    "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp",
    "OTEL_EXPORTER_OTLP_PROTOCOL": "grpc",
    "OTEL_EXPORTER_OTLP_ENDPOINT": "http://localhost:4317"
     },
   }
   ```

3. Open http://localhost:3000

## Commands

```bash
docker compose up -d      # Start
docker compose down       # Stop
docker compose logs -f    # View logs
docker compose down -v    # Reset (removes data)
```

## Services

| Service | Port | Description |
|---------|------|-------------|
| Grafana | 3000 | Dashboard UI |
| Prometheus | 9090 | Metrics storage |
| OTel Collector | 4317 | Receives metrics |
| Pushgateway | 9091 | Hook metrics | (WIP)
