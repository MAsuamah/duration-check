import subprocess

def get_duration_ffprobe(file_path):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                             '-of', 'default=noprint_wrappers=1:nokey=1', file_path], 
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return float(result.stdout)

def get_duration_mediainfo(file_path):
    result = subprocess.run(['mediainfo', '--Inform=General;%Duration%', file_path], 
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return float(result.stdout) / 1000  # Convert milliseconds to seconds

def get_duration_sox(file_path):
    result = subprocess.run(['sox', '--i', '-D', file_path], 
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return float(result.stdout)


file_path = 'audio.mp3'
duration_ffprobe = get_duration_ffprobe(file_path)
duration_mediainfo = get_duration_mediainfo(file_path)
duration_sox = get_duration_sox(file_path)


print(f"ffprobe duration: {duration_ffprobe}")
print(f"mediainfo duration: {duration_mediainfo}")
print(f"sox duration: {duration_sox}")
