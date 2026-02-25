# Deterministic Random Generator

This project provides a deterministic replacement for `/dev/urandom` in Docker containers for testing purposes.

## How It Works

The Python script `generate_rand.py` generates a predictable stream of bytes:
- It outputs a block of `0xAA` bytes (pattern 10101010)
- This pattern repeats indefinitely

## Usage

### Build the Docker Image

```bash
docker build -t deterministic-rand .
```

### Run the Container

```bash
docker run -it deterministic-rand
```

Inside the container, `/dev/urandom` will return the deterministic pattern instead of random data.

### Test It

Inside the container, you can test the deterministic random source:

```bash
# Read 10 bytes from /dev/urandom
head -c 10 /dev/urandom | xxd -ps

# Compare multiple reads (they should be identical at the same offset)
head -c 20 /dev/urandom | xxd -ps
```

### Customize Block Sizes

You can customize the sizes of the 1s and 0s blocks:

```bash
docker run -e COUNT=512 -it deterministic-rand
```

## Use Cases

- Testing cryptographic code with predictable input
- Debugging random number usage in applications
- Reproducible testing scenarios
- Analyzing behavior with specific byte patterns

## Warning

⚠️ **Never use this in production!** This completely removes randomness and makes any cryptographic operations insecure.
