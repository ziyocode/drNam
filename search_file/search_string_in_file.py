import os
import locale
from chardet import detect

include_ext_lists = [".txt", ".smi", ".py"]

current_locale = locale.getdefaultlocale()


def search(dirname, keyword, result_lists):
    filelist = os.listdir(dirname)
    for filename in filelist:
        full_filepath = os.path.join(dirname, filename)
        # print(full_filepath)

        if os.path.isdir(full_filepath):
            search(full_filepath, keyword, result_lists)
        else:
            # print(full_filepath)
            ext = os.path.splitext(full_filepath)[-1]

            if ext not in include_ext_lists:
                continue

            with open(full_filepath, "rb") as file:
                raw_data = file.read()
                encode = detect(raw_data)["encoding"]
                file_data = raw_data.decode(encode)
                # print(filename, encode, file_data)

                if file_data.find(keyword) >= 0:  # find 는 키워드의 위치를 반환 없을 경우 -1 반환
                    result_lists.append(full_filepath)


result = []
search("/tmp", "test", result)
print(result)
