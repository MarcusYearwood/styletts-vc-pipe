from config import cfg


def process_control():
    cfg['collate_mode'] = 'dict'
    data_shape = {'MNIST': [1, 28, 28], 'FashionMNIST': [1, 28, 28], 'SVHN': [3, 32, 32], 'CIFAR10': [3, 32, 32],
                  'CIFAR100': [3, 32, 32]}
    target_size = {'MNIST': 10, 'FashionMNIST': 10, 'SVHN': 10, 'CIFAR10': 10, 'CIFAR100': 100}
    cfg['linear'] = {}
    cfg['mlp'] = {'hidden_size': 128, 'scale_factor': 2, 'num_layers': 2, 'activation': 'relu'}
    cfg['cnn'] = {'hidden_size': [64, 128, 256, 512]}
    cfg['resnet9'] = {'hidden_size': [64, 128, 256, 512]}
    cfg['resnet18'] = {'hidden_size': [64, 128, 256, 512]}
    cfg['wresnet28x2'] = {'depth': 28, 'widen_factor': 2, 'drop_rate': 0.0}
    cfg['wresnet28x8'] = {'depth': 28, 'widen_factor': 8, 'drop_rate': 0.0}
    cfg['data_name'] = cfg['control']['data_name']
    cfg['data_shape'] = data_shape[cfg['data_name']]
    cfg['target_size'] = target_size[cfg['data_name']]
    cfg['model_name'] = cfg['control']['model_name']

    cfg['batch_size'] = 250
    cfg['step_period'] = 1
    cfg['num_steps'] = 80000
    cfg['eval_period'] = 200

    model_name = cfg['model_name']
    cfg[model_name]['shuffle'] = {'train': True, 'test': False}
    cfg[model_name]['optimizer_name'] = 'SGD'
    cfg[model_name]['lr'] = 1e-2
    cfg[model_name]['momentum'] = 0.9
    cfg[model_name]['betas'] = (0.9, 0.999)
    cfg[model_name]['weight_decay'] = 5e-4
    cfg[model_name]['nesterov'] = True
    cfg[model_name]['scheduler_name'] = 'CosineAnnealingLR'
    cfg[model_name]['batch_size'] = {'train': cfg['batch_size'], 'test': cfg['batch_size']}
    return
