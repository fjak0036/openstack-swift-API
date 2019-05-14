#swift�ɐڑ�

def cswift():
	import configparser #config�t�@�C������p�����[�^���擾����

	CONF_FILEPATH = 'swift_da_cfg.txt' #config file name

	config=configparser.ConfigParser()
	config.read(CONF_FILEPATH)#�R���t�B�O�t�@�C���̓ǂݍ���

	#�p�����[�^�A�T�C��
	auth_url = config.get('auth','auth_url')
	username = config.get('auth','username')
	password = config.get('auth','password')
	project_name =config.get('auth','project_name')
	user_domain_id =config.get('auth','user_domain_id')
	project_domain_id =config.get('auth','project_domain_id') 

	#�L�[�X�g���Eswift�p�b�P�[�W�C���|�[�g
#	from keystoneauth1 import session
	from keystoneauth1.identity import v3
#	from swiftclient import client

	#�L�[�X�g�[���@�g�[�N���𓾂�
	auth = v3.Password(auth_url=auth_url,
		username=username,
		password=password,
		project_name=project_name,
		user_domain_id=user_domain_id,
		project_domain_id=project_domain_id)

	
	print(auth)
	return auth

