# Song Querying by Humming
*A system to recognize choruses of songs from a user's hum*  
  
*EECS 352 || Machine Perception of Music || Professor Bryan Pardo || Northwestern University*

### Our Team
- Rohaan Advani || rohaanadvani2019@gmail.com
- Carlos Belardi || carlosbelardi2019@gmail.com
- Vishal Giridhar || vishalgiridhar2020@u.northwestern.edu

### Motivation
Most people have at some point in their life struggled with a song being stuck in their head, and no options to find out what its called. With most commercial systems these days, only when the song is played in real-time would it be able to recognize it and label it with the title. SoundHound is the only well-known method that exists to query a song by humming, even though a number of research papers have been written on said topic. As a result, we were curious if we could create our own query-by-humming systeem. We believe the chorus is the most distinguishable part of a song, and is the melody that is most likely to be ingrained into a listener's mind.

When it comes to how our code works. For both the humming audio and all of our songs, we create a chromagram. This chromagram shows 12 notes per sample (0.2 secs), and each note has a value from 0-1 relating to how prevalent that note is. We find the most prominent note for each sample, and create a waveform using those. Pattern match with cosine distance of hum, and of each song. Our goal is for the song to bee in the top 10  
