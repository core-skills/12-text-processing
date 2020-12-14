import io
import base64
from pathlib import Path
import gzip
import shutil
from urllib.request import urlopen
from io import BytesIO
import pandas as pd
import tqdm
import zlib


# list of filepaths for local storage mapped to their remote equivalents, noting compression
MANIFEST = {
    "../data/glove.6B.50d.txt": (
        "https://1drv.ms/u/s!As2ibEui13xml4JKELeEITUmX0WUHQ?e=kp6Yw9",
        True,
    ),
    "../data/reviews_data.txt": (
        "https://1drv.ms/u/s!As2ibEui13xml4JJ2vVIJqveOf28kQ?e=TFpGfz",
        True
    ),
    "../data/wamex_xml.zip" : (
        "https://1drv.ms/u/s!As2ibEui13xml4JEufgSyii95XLACA?e=CAp9a6", 
        False
    ),
    "../data/word2vec/word2vec_gswa.bin": (
        "https://1drv.ms/u/s!As2ibEui13xml4JIZY6jGXoSmCJgaw?e=WreJmt",
        False
    ),
    "../data/word2vec/word2vec_reviews.bin": (
        "https://1drv.ms/u/s!As2ibEui13xml4JDKG5Alk1YGqgMVg?e=6JS4iJ",
        False
    ),
    "../data/word2vec/word2vec_reviews.bin.trainables.syn1neg.npy": (
        "https://1drv.ms/u/s!As2ibEui13xml4JH8Gy7XtU_uvU3WA?e=aS2BNw",
        False
    ),
    "../data/word2vec/word2vec_reviews.bin.wv.vectors.npy": (
        "https://1drv.ms/u/s!As2ibEui13xml4JG_eV7vHv84U_MVg?e=W5OG6H",
        False
    ),
}


def get_onedrive_directlink(onedrive_link):
    """
    Get a public Onedrive filehandle for linking directly to pandas.

    Parameters
    -----------
    onedrive_link : str
        Onedrive share URL.

    Returns
    -------
    direct_url
        Base64-encoded URL for direct download/for use as a file handle.

    Notes
    -----
    Found here:
    https://towardsdatascience.com/how-to-get-onedrive-direct-download-link-ecb52a62fee4
    """
    data_bytes64 = base64.b64encode(bytes(onedrive_link, "utf-8"))
    data_bytes64_string = (
        data_bytes64.decode("utf-8").replace("/", "_").replace("+", "-").rstrip("=")
    )
    direct_url = "https://api.onedrive.com/v1.0/shares/u!{}/root/content".format(
        data_bytes64_string
    )
    return direct_url


def compress(filepath):
    """Compress a text file to a gzipped copy (.txt.gz) locally"""
    with open(filepath, "rb") as f_in:
        with gzip.open(filepath.with_suffix(".txt.gz"), "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)


def fetch_file(name, chunksize=16 * 1024):
    """
    Fetch a datafile from a compressed/gzipped URL source.

    Parameters
    ----------
    name : :class:`str`
        Name of the file to fetch.
    chunksize : :class:`int`
        Number of bytes to read in a chunk.
    """
    fp, url, compressed = [
        (Path(k), url, compressed)
        for (k, (url, compressed)) in MANIFEST.items()
        if name.lower() in Path(k).name.lower()
    ][0]
    if "1drv" in url:
        url = get_onedrive_directlink(
            url
        )  # allow direct access to file object for 1drv
    # construct relative path from this file
    local_target = (Path(__file__).parent / fp).resolve()

    if not local_target.exists():
        if not local_target.parent.exists():
            local_target.parent.mkdir(parents=True)
        if compressed:
            dec = zlib.decompressobj(
                32 + zlib.MAX_WBITS
            )  # offset 32 to skip the header
            decompress = dec.decompress
        else:
            decompress = lambda x: x

        with urlopen(url) as response:
            pbar = tqdm.tqdm(
                total=int(response.headers["content-length"]),
                unit="b",
                unit_scale=True,
                unit_divisor=1024,
                desc=str(fp.name),
            )
            CHUNKSIZE = 16 * 1024
            with open(local_target, "wb") as f:
                while True:
                    chunk = response.read(chunksize)
                    if chunk:
                        rv = decompress(chunk)
                        f.write(rv)
                        pbar.update(len(chunk))
                    else:
                        break
    return fp


# if run directly, fetch everything
if __name__ == "__main__":
    for fp, url in MANIFEST.items():

        fetch_file(Path(fp).name)
