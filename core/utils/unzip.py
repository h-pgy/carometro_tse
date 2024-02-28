import tempfile
from typing import List, Generator
from io import BytesIO
from tempfile import TemporaryDirectory, NamedTemporaryFile
from zipfile import ZipFile
import os

def unzip_from_bytes(content:bytes, members_to_extract:List[str]=None)->Generator[str, str, str]:

    with TempZip(content) as tempzip:
        with TempUnZipper(tempzip, members_to_extract) as tempunzip:
            for file in tempunzip:
                yield file

class TempZip:

    def __init__(self, content:bytes):

        self.tempfile = self.__create_tempfile()
        self.__write_to_temp(content)
        self.zipfile = self.__gen_zipfile()

    def __create_tempfile(self)->NamedTemporaryFile:

        return NamedTemporaryFile()

    def __write_to_temp(self, content:bytes):

        self.tempfile.write(content)

    def __gen_zipfile(self):

        return ZipFile(self.tempfile.name)
    
    def __enter__(self)->ZipFile:

        return self.zipfile
    
    def __exit__(self,  type, value, traceback)->None:

        self.zipfile.close()
        self.tempfile.close()


class TempUnZipper:

    def __init__(self, zipfile:ZipFile, members_to_extract:List[str]=None)->None:

        self.tempdir =  self.__create_tempdir()
        self.extract(zipfile, members_to_extract)
        
    def __create_tempdir(self)->TemporaryDirectory:

        return tempfile.TemporaryDirectory()
    
    def close_tempdir(self)->None:

        self.tempdir.cleanup()
    
    def __unziped_file_gen(self)->Generator[str, str, str]:

        try:
            for file in os.listdir(self.tempdir.name):
                yield os.path.abspath(os.path.join(self.tempdir.name, file))
        finally:
            self.close_tempdir()
    
    def __check_member(self, zipfile:ZipFile, member:str)->None:

        if member not in zipfile.filelist():
            raise RuntimeError(f'Arquivo {member} não existe no zipfile.')

    def __extract_member(self, zipfile:ZipFile, member:str, tempdir:TemporaryDirectory)->None:

        self.__check_member(zipfile, member)
        zipfile.extract(member, tempdir)

    def extract(self, zipfile:ZipFile, members:List[str]=None)->None:

        if members is None:
            zipfile.extractall(self.tempdir.name)
        else:
            for member in members:
                self.__extract_member(zipfile, member, self.tempdir)

    def __enter__(self)->Generator[str, str, str]:

        return self.__unziped_file_gen()
    
    def __exit__(self, type, value, traceback)->None:

        self.close_tempdir()
