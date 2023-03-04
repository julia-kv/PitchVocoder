import logging
import click

import librosa
import sys
import soundfile as sf
import vocoder

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)


def stretch_wav(input_file, output_file, time_stretch_ratio):

    try:
        wav, sample_rate = librosa.load(input_file)
    except:
        logger.exception(f'Error while loading file - {input_file}')
        sys.exit(-1)

    transformed_wav = vocoder.vocoder_algorithm(wav, time_stretch_ratio)

    sf.write(output_file, transformed_wav, int(sample_rate))


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file')
@click.argument('compression_param')
def main(input_file, output_file, compression_param):
    stretch_wav(input_file, output_file, float(compression_param))


if __name__ == '__main__':
    main()
