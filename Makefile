.PHONY: tag build

build:
	tito build --rpm --dist .el7

tag:
	tito tag
	git push origin master
	git push --tags
