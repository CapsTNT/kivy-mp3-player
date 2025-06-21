# main.py
import os
import random
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from ffpyplayer.player import MediaPlayer

MUSIC_FOLDER = "E:/MTC/Music/Instrumental/Geometry dash"

class MP3PlayerApp(App):
    def build(self):
        self.songs = self.find_mp3_files(MUSIC_FOLDER)
        random.shuffle(self.songs)
        self.current_index = 0
        self.player = None
        self.paused = False

        # UI
        self.label = Label(text="🎵 No song playing", size_hint=(1, 0.2))
        self.play_button = Button(text="▶ Play", on_press=self.play_song)
        self.pause_button = Button(text="⏸ Pause / Resume", on_press=self.pause_resume)
        self.next_button = Button(text="⏭ Next", on_press=self.next_song)

        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        layout.add_widget(self.label)
        layout.add_widget(self.play_button)
        layout.add_widget(self.pause_button)
        layout.add_widget(self.next_button)

        # Start polling player status
        Clock.schedule_interval(self.check_player, 1.0)

        return layout

    def find_mp3_files(self, folder):
        return [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if f.lower().endswith('.mp3')
        ]

    def play_song(self, instance=None):
        self.stop_player()

        if not self.songs:
            self.label.text = "❌ No songs found!"
            return

        song_path = self.songs[self.current_index]
        self.player = MediaPlayer(song_path)
        self.paused = False
        self.label.text = f"🎶 Now Playing: {os.path.basename(song_path)}"

    def pause_resume(self, instance=None):
        if self.player:
            self.paused = not self.paused
            self.player.set_pause(self.paused)
            self.label.text = "⏸️ Paused" if self.paused else "▶️ Resumed"

    def next_song(self, instance=None):
        self.stop_player()
        self.current_index = (self.current_index + 1) % len(self.songs)
        self.play_song()

    def stop_player(self):
        if self.player:
            try:
                self.player.close_player()
            except:
                pass
            self.player = None

    def check_player(self, dt):
        if self.player and not self.paused:
            frame, val = self.player.get_frame()
            if val == 'eof':
                self.next_song()

if __name__ == '__main__':
    MP3PlayerApp().run()
