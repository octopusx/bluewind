# bluewind

Bluetooth control app for Wahoo Headwind.

To run the flask app:
```bash
flask --app api run --host=0.0.0.0
```

To use the cli:
```bash
./cli.py --help
./cli.py --address <bt_address> --cmd <on/sleep>
./cli.py --address <bt_address> --cmd manual --speed <1-100>
```
