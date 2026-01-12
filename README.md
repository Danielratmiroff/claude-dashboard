# Claude Code Metrics Dashboard

Grafana dashboard for visualizing Claude Code usage metrics.

<img width="1446" height="1240" alt="Pasted image 20260109100843" src="https://github.com/user-attachments/assets/93825254-8b60-4d0e-af89-fb568e0d9d04" />

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
| Pushgateway | 9091 | Hook metrics (WIP) | 
