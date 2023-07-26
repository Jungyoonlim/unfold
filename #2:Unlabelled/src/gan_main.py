import argparse
from data_process import load_data
from models import make_generator_model, make_discriminator_model
from training import train, generator_optimizer, discriminator_optimizer
from config import EPOCHS, noise_dim
import tensorflow as tf

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default='default_dataset',
                        help='The name of the dataset to use')
    parser.add_argument('--epochs', type=int, default=EPOCHS,
                        help='The number of training epochs')
    parser.add_argument('--noise_dim', type=int, default=noise_dim,
                        help='The dimensionality of the noise vector')
    args = parser.parse_args()
    
    print(f'Loading dataset: {args.dataset}')
    dataset = load_data(args.dataset)
    
    print('Creating models...')
    generator = make_generator_model()
    discriminator = make_generator_model()
    
    print('Starting training...')
    try:
        train(dataset, generator, discriminator, generator_optimizer, discriminator_optimizer, args.epochs, args.noise_dim)
    except Exception as e:
        print(f'Error during training: {e}')
        raise
    else:
        print('Training completed successfully')

if __name__ == "__main__":
    main()
