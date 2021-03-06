import torch
import numpy as np
import random
import hydra


from omegaconf import DictConfig, OmegaConf
from utils import get_mnist, train_loop, test_loop, init_obj

@hydra.main(config_path="./config/", config_name="configs.yaml")
def main(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))

    torch.manual_seed(cfg.seed)
    np.random.seed(cfg.seed)
    random.seed(cfg.seed)

    model = hydra.utils.instantiate(cfg.model)

    loss_fn = torch.nn.CrossEntropyLoss()

    #optimizer = hydra.utils.instantiate(cfg.optimizer)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.learning_rate)
    #opt_params = dict(cfg.optimizer)
    #opt_params['params'] = model.parameters()
    #optimizer = init_obj(cfg.optimizer, opt_params)

    train_data, test_data = get_mnist(batch_size=cfg.batch_size)

    for epoch in range(cfg.num_epochs):
        print(f"Epoch {epoch + 1}\n-------------------------------")
        train_loop(train_data, model, loss_fn, optimizer)

    #if (epoch + 1) % 20 == 0:
        #curr_lr /= 3
        #update_lr(optimizer, curr_lr)

        test_loop(test_data, model, loss_fn)

if __name__ == "__main__":
    main()
