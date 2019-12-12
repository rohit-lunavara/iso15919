
# Transcript of Guj-78 type -> Transcript of Tedlium type

# def transcript_conv(source) : return '' #stub

# signature
# def transcript_conv(source_trans) :
#    return tedlium_trans
import wave
import contextlib
# Transliteration module
import iso15919

def transcript_conv(source_trans) :
    # Gujarati male
    fhand = open(source_trans, 'r', encoding = 'utf-8')
    # file_id 1 speaker_id start_time end_time <overall_results, channel_type, speaker_gender> transcript
    stmout = ''
    tedlium_trans = ''

    for row in fhand :
        file_id, transcript = row.split('\t')
        
        # Extract speaker_id
        speaker_id = 'guj-78-m-' + file_id.split('_')[1]
        #print(speaker_id)

        # Open file with name file_id.wav and get start_time, end_time
        #wavname = 'guj-78/' + file_id + '.wav'
        #with contextlib.closing(wave.open(wavname,'r')) as f:
        #    frames = f.getnframes()
        #    rate = f.getframerate()
        #    duration = frames / float(rate)
        #    starttime = 0
        #    endtime = round(duration, 2)

        # Set all other attributes
        overall_results = 'o'
        channel_type = 'f0'
        speaker_gender = 'male'

        # Romanize transcript
        #quit()
        print(transcript)
        print(iso15919.transliterate(str(transcript)), end = '\n\n')

    fhand.close()
    return tedlium_trans

x = 2
if x == 1 :
    transcript_conv('guj-78/line_index.tsv')
else :
    hindi_text = u'हिंदी टायपिंग અદેપુર ગામના લોકોનો મુખ્ય વ્યવસાય ખેતી છે.'
    print(iso15919.transliterate(hindi_text))