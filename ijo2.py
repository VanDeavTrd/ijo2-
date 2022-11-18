from rich import print as cetak
import os
if __name__ == "__main__":
	try:
		os.system("git pull")
	except Exception as e:
		exit(str(e))
cetak(f"[bold green] MAAF SCRIPT INI SUDAH DI TUTUP 🙏🏻 ")