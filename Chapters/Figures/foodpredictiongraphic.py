import matplotlib.pyplot as plt
import numpy as np

spl = np.arange(20, 75, 5)

music_mean = np.array([-0.5, -0.6, -0.7, -0.8, -0.9, -1.0, -1.1, -1.2, -1.3, -1.4, -1.5])
music_ci = np.array([0.5, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5])

wn_mean = np.array([-0.4, -0.4, -0.4, -0.4, -0.5, -0.6, -0.7, -0.7, -0.8, -0.9, -1.0])
wn_ci = np.array([0.4, 0.4, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4])

pn_mean = np.array([-0.4, -0.5, -0.5, -0.6, -0.6, -0.7, -0.7, -0.8, -0.8, -0.8, -0.9])
pn_ci = np.array([0.4, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4])

cs_mean = np.array([-0.3, -0.3, -0.4, -0.4, -0.4, -0.5, -0.5, -0.6, -0.6, -0.7, -0.7])
cs_ci = np.array([0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4])

fig, axs = plt.subplots(2, 2, figsize=(10, 8), sharex=True, sharey=True)

axs[0, 0].plot(spl, music_mean, label="Mean")
axs[0, 0].fill_between(spl, music_mean - music_ci, music_mean + music_ci, alpha=0.5, label="95% CI")
axs[0, 0].set_ylabel("Relative food liking")
axs[0, 0].set_title("a) Music")
axs[0, 0].legend()

axs[0, 1].plot(spl, wn_mean, label="Mean")
axs[0, 1].fill_between(spl, wn_mean - wn_ci, wn_mean + wn_ci, alpha=0.5, label="95% CI")
axs[0, 1].set_title("b) Restaurant noise")

axs[1, 0].plot(spl, pn_mean, label="Mean")
axs[1, 0].fill_between(spl, pn_mean - pn_ci, pn_mean + pn_ci, alpha=0.5, label="95% CI")
axs[1, 0].set_ylabel("Relative food liking")
axs[1, 0].set_xlabel("SPL (dBA)")
axs[1, 0].set_title("c) Road traffic noise")

axs[1, 1].plot(spl, cs_mean, label="Mean")
axs[1, 1].fill_between(spl, cs_mean - cs_ci, cs_mean + cs_ci, alpha=0.5, label="95% CI")
axs[1, 1].set_xlabel("SPL (dBA)")
axs[1, 1].set_title("d) All stimuli")

plt.tight_layout()

plt.savefig("foodprediction.pdf")

plt.show()