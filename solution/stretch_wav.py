import logging
# import click

import librosa
import sys
import soundfile as sf
import vocoder


def stretch_wav():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    time_stretch_ratio = float(sys.argv[3])

    try:
        wav, sample_rate = librosa.load(input_file)
    except:
        logging.error(f'File {input_file} does not exist')
        sys.exit(-1)

    transformed_wav = vocoder.vocoder_algorithm(wav, time_stretch_ratio)

    sf.write(output_file, transformed_wav, int(sample_rate))


# @click.command()
# @click.argument('input_file')
# @click.argument('output_file')
# @click.argument('compression_param')
# def main(input_file, output_file, compression_param):
#     compress_wav(input_file, output_file, float(compression_param))


if __name__ == '__main__':
    stretch_wav()
