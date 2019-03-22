# Song Querying by Humming
*A system to recognize choruses of songs from a user's hum*  
  
*EECS 352 || Machine Perception of Music || Professor Bryan Pardo || Northwestern University*

### Our Team
- Rohaan Advani || rohaanadvani2019@gmail.com
- Carlos Belardi || carlosbelardi2019@gmail.com
- Vishal Giridhar || vishalgiridhar2020@u.northwestern.edu

### Motivation
Most people have at some point in their life struggled with a song being stuck in their head, and no options to find out what its called. With most commercial systems these days, only when the song is played in real-time would it be able to recognize it and label it with the title. SoundHound is the only well-known method that exists to query a song by humming, even though a number of research papers have been written on said topic. As a result, we were curious if we could create our own query-by-humming systeem. We believe the chorus is the most distinguishable part of a song, and is the melody that is most likely to be ingrained into a listener's mind.

### Our Journey
When it comes to how our code works. For both the humming audio and all of our songs, we create a chromagram. This chromagram shows 12 notes per sample (0.2 secs), and each note has a value from 0-1 relating to how prevalent that note is. We find the most prominent note for each sample, and create a waveform using those. Once the waveform is created, we do pattern matching by calculating the cosine distance between our hum and each song. We then return the songs with the top 10 scores, and ideally the song we're looking for is in those results.

Our process for developing this approach was quite hectic. We began with a completely different approach where we used the Melodia and Vamp python libraries to extract the melody of each song, and get a frequency array of those melodies. Once we had those frequencies, we kept track of the changes in frequencies with three string options: 'u'=up, 's'=same, and 'd'=down. We created arrays of these frequency changes for our hum samples, and for our initial database which contained the .wav files of 10 songs. At first we were getting really good results, with our correct song showing up in the top 3 results for each of the three humming samples we had. However, when we expanded our database to include all 50 songs we wanted, our results deteriorated completely. Now the correct songs weren't even in the top 10 results, which is not good.

We quickly pivoted and tried to do many different things to try and get better results. The first decision we made was to scale down the project, and focus only on song choruses. Then we tried performing an STFT on our wave file, then using a similar frequency change algorithm but got poor results. We also tried using all of the chromagram information, rather than finding the highest value but that didn't work well. Finally we tried pattern matching waveforms with cross-correlation instead of cosine but also got subpar results. Through this trial and error we got our final approach of extracing the notes from the chromagram, creating waveforms, and calculating the cosine distance. 

### Results


### Image
![image](AmericanBoy.png)

In this graph for the song American Boy we can see the two waveforms we've created, and one can see how some parts of the hum waveform perfectly match the chorus waveform if it were shifted over a bit. This is taken into consideration in our cosine distance calculation and when a hum has a graph like this, it's usually a sign that it'll have a high score.

### Audio Samples

Here are some humming samples that worked well, along with their respective chorus

[Call Me Maybe Hum](https://raw.githubusercontent.com/weeshal/eecs352-final/master/Hum/CallMeMaybeHum.wav)

[Call Me Maybe Chorus](/Chorus/CallMeMaybeChorus.wav)


[American Boy Hum](/Hum/AmericanBoyHum.wav)

[American Boy Chorus](/Chorus/AmericanBoyChorus.wav)


Here are some humming samples that didn't work well, which we mainly found to be hip hop songs

[Congratulations Hum](/Hum/CongratulationsHum.wav)

[Congratulations Chorus](/Chorus/CongratulationsChorus.wav)


[Bodak Yellow Hum](/Hum/BodakYellowHum.wav)

[Bodak Yellow Chorus](/Chorus/BodakYellowChorus.wav)
