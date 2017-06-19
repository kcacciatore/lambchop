
notes = [ 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#' ]

degrees = {'r' : 0, 'h': 1, 'w': 2, 'wh': 3}

scales = { 'major' : ['r','w','w','h','w','w','w','h'],
           'minor' : ['r','w','h','w','w','h','w','w'],
           'harmonic minor' : ['r','w','h','w','w','h','wh','h'],
           'melodic minor up' : ['r','w','h','w','w','w','w','h'],
           'melodic minor down' : ['r','w','w','h','w','w','h','w'],
           'ionian'     : ['r','w','w','h','w','w','w','h'],
           'dorian'     : ['r','w','h','w','w','w','h','w'],
           'phrygian'   : ['r','h','w','w','w','h','w','w'],
           'lydian'     : ['r','w','w','w','h','w','w','h'],
           'mixolydian' : ['r','w','w','h','w','w','h','w'],
           'aeolian'    : ['r','w','h','w','w','h','w','w'],
           'locrian'    : ['r','h','w','w','h','w','w','w'],
          }

def scale_degree(scale, d):
    ''' Given a scale and degree, return the number of semitones to move
    '''
    #print('Calculating %i degree of %s scale' % (d, scale))
    scale_pattern = scales.get(scale)
    semitones = 0
    for i in range(d+1):
        #print('value for %i is %i ' % (i, degrees.get(scale_pattern[i])))
        semitones += degrees.get(scale_pattern[i])
    #print('%d degree of %s scale is %d' % (d, scale, semitones))
    return semitones


def build_scale(target_scale, key):
    scale = []
    scale_pattern = scales.get(target_scale)
    for i in range(len(scale_pattern)):
        semitones = scale_degree(target_scale,i)
        #print('Root at %d ' % notes.index(key))
        #print('Semitones %d ' % semitones)
        index = (notes.index(key) + semitones) % len(notes)
        #print(index)
        scale.append(notes[index])
    return scale


def main():
    print("lydian scale\t%s" % build_scale('lydian','C'))
    print("ionian scale\t%s " % build_scale('ionian','C'))
    print("mixo scale\t%s" % build_scale('mixolydian','C'))
    print("dorian scale\t%s" % build_scale('dorian','C'))
    print("aeolian scale\t%s" % build_scale('aeolian','C'))
    print("phrygian scale\t%s" % build_scale('phrygian','C'))
    print("locrian scale\t%s" % build_scale('locrian','C'))

if __name__ == '__main__':
    main()
