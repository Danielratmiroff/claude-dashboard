# Claude Code Metrics Dashboard

## Documentation

Use exploration capabilities to explore the documentation when needed.

- Claude Code Monitoring Usage: https://code.claude.com/docs/en/monitoring-usage
- Grafana Provisioning: https://grafana.com/docs/grafana/latest/administration/provisioning/

## Testing

after updating the dashboard, it needs to be updated via API.

```bash
curl -X POST -H "Content-Type: application/json" \
  -d "{\"dashboard\": $$(cat /dashboards/claude-code.json), \"overwrite\": true}" \
  http://grafana:3000/api/dashboards/db
```