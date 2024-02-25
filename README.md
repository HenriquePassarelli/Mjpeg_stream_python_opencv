# Mjpeg_stream_python_opencv

Using Python along with opencv to read any kind of video and stream it as Mjpeg

> Consider it as a simple Mjpeg server.

### Make sure you have
```
sudo apt install python3

sudo apt install python3-pip
```

### Install dependencies
```
pip3 install -r requirements.txt
```

### run script

```
python3 main.py 
# or
python3 main.py --port <port>   
```

### How to use
After starting the server you can choose one of the API calls, every API call is need to pass in the url the video url as base64, with that it will return a Mjpeg stream 

```
http://localhost:5000/stream?url=<base64 url>
```

# Disclaimer

It's for test, so the video fps, frame rate and performance can be slowed down
