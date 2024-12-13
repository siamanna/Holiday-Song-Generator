from midiutil import MIDIFile
import markovify
import random

# Step 1: Generate Lyrics using Markov Chain
def generate_lyrics():
    holiday_songs = """
    Jingle bells, jingle bells, jingle all the way
    Oh, what fun it is to ride in a one-horse open sleigh hey
    Deck the halls with boughs of holly
    Fa-la-la-la-la, la-la-la-la
    Joy to the world, the Lord has come
    Let earth receive her King
    Silent night, holy night
    All is calm, all is bright
    Here comes Santa Claus here comes Santa Claus
    I saw Mommy kissing Santa Claus
    """
    text_model = markovify.Text(holiday_songs)
    lyrics = [text_model.make_sentence() or "Fa-la-la, la-la-la" for _ in range(4)]
    return "\n".join(lyrics)

def create_melody(output_file="holiday_song.mid"):
    midi = MIDIFile(1)  
    track = 0
    time = 0  
    tempo = 120  
    channel = 0
    volume = 100

    midi.addTempo(track, time, tempo)

    notes = [60, 62, 64, 65, 67, 69, 71, 72]  
    duration = 1 

    for i in range(16):
        note = random.choice(notes)
        midi.addNote(track, channel, note, time, duration, volume)
        time += duration

    with open(output_file, "wb") as output:
        midi.writeFile(output)
    print(f"🎶 Melody saved to {output_file}")

def main():
    print("✨ Generating Holiday Song Lyrics...\n")
    lyrics = generate_lyrics()
    print("🎤 Holiday Lyrics:")
    print(lyrics)
    
    print("\n🎶 Creating Holiday Melody...")
    create_melody()
    print("\n✨ Your holiday song is ready! 🎄")

if __name__ == "__main__":
    main()
