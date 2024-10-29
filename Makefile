# Makefile for Rust Project


all: check build test install lint format


check:
	cargo check

build:
	cargo build

format:
	cargo fmt
	black *.py
	black library/*.py 

lint:
	cargo clippy
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py library/*.py

test:
	cargo test
	python -m pytest -vv --cov=main --cov=library test_*.py

release:
	cargo build --release

install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt
	