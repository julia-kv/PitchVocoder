import numpy as np
import librosa


def phase_shift(input_hop: int, output_hop: int, frames: np.ndarray) -> np.ndarray:
    transformed_frames = []

    last_phase = 0
    phase_accumulator = 0

    for frame in frames:
        freq_bins = 2 * np.pi * np.arange(len(frame)) / len(frame)

        # we want to change frequency from changing phase in polar coords
        # extract magnitude and phase
        magnitude, phase = np.abs(frame), np.angle(frame)

        # calculate difference with previous
        delta_phase = phase - last_phase
        last_phase = phase

        # re-wrap new phase delta
        delta_freq_unwrapped = delta_phase / input_hop - freq_bins
        delta_freq_rewrapped = np.mod(delta_freq_unwrapped + np.pi, 2 * np.pi) - np.pi

        true_freq = freq_bins + delta_freq_rewrapped
        phase_accumulator += output_hop * true_freq

        # recalculate in polar coords
        transformed_frames.append(magnitude * np.exp(phase_accumulator * 1j))

    return np.array(transformed_frames)


def vocoder_algorithm(wav: np.ndarray, compression: float) -> np.ndarray:
    # set parameters
    CHUNK_SIZE = 4096

    HOP = int(CHUNK_SIZE / 4)
    HOP_OUT = int(HOP * compression)


    # ANALYSIS
    frames = librosa.stft(wav, n_fft=CHUNK_SIZE, hop_length=HOP)

    # PROCESSING
    transformed_wav = phase_shift(HOP, HOP_OUT, frames)

    # SYNTHESIS
    transformed_wav = librosa.istft(transformed_wav, hop_length=HOP_OUT)

    return transformed_wav
