import os
import re


def bytes_to_megabytes_string(size: int) -> str:
    size_in_mb: float = size / 1000000
    formatted_str: str = "{:.2f}MB".format(size_in_mb)
    return formatted_str


def user_accepts_action(input: str, action, alternative):
    if input.lower() in ["yes", "y"]:
        action()
    else:
        alternative()


def delete_files(files):
    for f in files:
        print(f"{f[0]} has been deleted 💀")


username = os.getlogin()
downloadspath = f"/Users/{username}/Downloads/"
files = [
    (f, os.path.getsize(f"{downloadspath}/{f}"), f"{downloadspath}/{f}")
    for f in os.listdir(downloadspath)
]

duplicates = [
    (f[0], bytes_to_megabytes_string(f[1]), f[2])
    for f in files
    if re.search(r"\([0-9]\)", f[0].split(".")[0])
]

print(
    f"{username}, there are a total of {len(files)} files in your Downloads directory, including {len(duplicates)} duplicated files."
)
user_input = input("Would you like to delete all duplicates? [Y/N]: ")
if user_input.lower() in ["yes", "y"]:
    for f in duplicates:
        print(f"{f[0]} - {f[1]}")
    confirmation_input = input(
        "[WARNING]: The above files will be deleted, confirm you wish to delete these? [Y/N]:"
    )
    user_accepts_action(
        confirmation_input, lambda: delete_files(duplicates), lambda: None
    )


# for f in files:
#     duplicate = False
#     size = os.path.getsize(f[2])
#     size_in_mb_str = bytes_to_megabytes_string(size)
#     atime = os.path.getatime(f[2])
#     if re.search(r"\([0-9]\)", f[0].split(".")[0]):
#         duplicate = True
#     print(f"{f[0]} size={size_in_mb_str}MB, last accessed={atime}")
#     if duplicate:
#         print("\t\t\tDUPLICATE")
