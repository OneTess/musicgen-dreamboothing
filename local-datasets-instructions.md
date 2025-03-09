[GitHub link](https://github.com/ylacombe/musicgen-dreamboothing?tab=readme-ov-file#how-do-i-use-audio-files-that-i-have-with-your-training-code) 

## QUOTE: 

How do I use audio files that I have with your training code?
If you song files in your computer, and want to create a dataset from datasets with those, you can use easily do this.

    You first need to create a csv file that contains the full paths to the audio. The column name for those audio files could be for example audio.
    Once you have this csv file, you can load it to a dataset like this:

from datasets import DatasetDict

dataset = DatasetDict.from_csv({"train": PATH_TO_CSV_FILE})

    You then need to convert the audio column name to Audio so that datasets understand that it deals with audio files.

from datasets import Audio
dataset = dataset.cast_column("audio", Audio())

    You can then save the datasets locally or push it to the hub:

dataset.push_to_hub(REPO_ID)

Note that you can make the dataset private by passing private=True to the push_to_hub method. Find other possible arguments here.

---

## NOTE: Apparently the expected action sequence is:
1. Create the csv file listing paths to all the training samples.
2. Load the csv file to a dataset: 
```
from datasets import DatasetDict
dataset = DatasetDict.from_csv({"train": PATH_TO_CSV_FILE})
```
3. CONVERT the audio column name to **Audio** class so that **datasets** understands it is dealing with audio files. [More info](https://huggingface.co/docs/datasets/v2.19.0/en/package_reference/main_classes#datasets.Audio)
```
from datasets import Audio
dataset = dataset.cast_column("audio", Audio())
```
4. SAVE the dataset LOCALLY -- after converting a folder with raw audio files into an **Audio** object.

In the code, the dataset is loaded with:
```
# 1. First, let's load the dataset
    raw_datasets = DatasetDict()
    num_workers = data_args.preprocessing_num_workers
    add_metadata = data_args.add_metadata
```

And you are **APPARENTLY** supposed to provide this **dataset** variable. This variable being the converted dataset **Audio** object.
```
dataset.save_to_disk("/home/onetessone/ai/musicgen-dreamboothing/datasets/0007-dataset")
```

And then in the terminal command to run musicgen_dreamboothing.py you specify the dataset path: 
```
--dataset_name "/home/onetessone/ai/musicgen-dreamboothing/datasets/0007-dataset" \
```