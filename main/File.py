class CosPlayFile():
    name = ''
    p_count = 0
    v_count = 0
    f_size = 0
    download_url = ''

    def __init__(self,_name,_p_count,_v_count,_f_size,_download_url):
        self.name = _name
        self.p_count = _p_count
        self.v_count = _v_count
        self.f_size = _f_size
        self.download_url = _download_url

    def __setName__(self,_name):
        self.name = _name
        return self

    def __setPCount__(self,_p_count):
        self.p_count = _p_count
        return self

    def __setVCount__(self,_v_count):
        self.v_count = _v_count
        return self

    def __setFSize__(self,_f_size):
        self.f_size = _f_size
        return self

    def __setDownLoadUrl__(self,_download_url):
        self.download_url = _download_url
        return self
