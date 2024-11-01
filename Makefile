# Makefile for Rust Project


all: check build test install lint format


check:
	cargo check

build:
	cargo build

format:
	cargo fmt
	black python_process/*.py 


lint:
	cargo clippy
	pylint --disable=R,C --ignore-patterns=test_.*?py $(shell find . -name "*.py")


test:
	cargo test
	python -m pytest -vv --cov=main --cov=python_process/test_*.py

release:
	cargo build --release

install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt



	