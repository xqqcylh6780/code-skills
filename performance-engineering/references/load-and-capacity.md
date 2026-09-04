# Load and Capacity

Load testing should answer a bounded question, not simply generate the largest number possible.

Define:

```text
traffic/workload model:
arrival/concurrency pattern:
dataset/state:
ramp/steady behavior:
latency/error target:
resource/saturation signals:
maximum safe test bound:
stop condition:
```

Increase load gradually and observe where latency, errors, queueing, memory, CPU, database connections, locks, or external dependencies saturate.

Do not extrapolate linearly beyond the measured range when queueing, caches, pools, GC, rate limits, database plans, or autoscaling can change behavior.

Never load-test production or a third-party API without explicit authorization and a defined safety envelope.
