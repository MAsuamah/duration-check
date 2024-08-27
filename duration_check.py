import subprocess

def get_duration_ffprobe(file_path):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                             '-of', 'default=noprint_wrappers=1:nokey=1', file_path], 
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return float(result.stdout)

file_path = 'audio.mp3'
duration_ffprobe = get_duration_ffprobe(file_path)

print(f"ffprobe duration: {duration_ffprobe}")
