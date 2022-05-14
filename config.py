import configargparse

def get_life_args():

    parser = configargparse.ArgParser(config_file_parser_class=configargparse.YAMLConfigFileParser)
    parser.add_argument('--iters', type=int, default=12)
    parser.add_argument('--mixed_precision', type=bool, default=True)
    parser.add_argument('--small', action='store_true', help='use small model')
    parser.add_argument('--model', type=str, default="./model/pretrain.pth", help="choose the trained model")    

    args = parser.parse_known_args()[0]
    return args

def get_raft_args():
    #parser = argparse.ArgumentParser()
    parser = configargparse.ArgParser(config_file_parser_class=configargparse.YAMLConfigFileParser)
    parser.add_argument("--mixed_precision", type=bool, default=True, required=False)
    parser.add_argument("--small", type=str, default=False, required=False)
    parser.add_argument("--iters", type=int, default=12, required=False)
    parser.add_argument("--dim_corr", type=int, default=192, required=False)
    parser.add_argument("--dim_corr_coarse", type=int, default=64, required=False)
    parser.add_argument("--dim_corr_all", type=int, default=256, required=False)    
    parser.add_argument("--model", type=str, default="./model/RAFT_latest.pth", required=False)

    args = parser.parse_known_args()[0]
    return args

def get_twins_args():
    #parser = argparse.ArgumentParser()
    parser = configargparse.ArgParser(config_file_parser_class=configargparse.YAMLConfigFileParser)
    parser.add_argument("--mixed_precision", type=str, default=True, required=False)
    parser.add_argument("--small", type=str, default=False, required=False)
    parser.add_argument("--iters", type=int, default=12, required=False)
    parser.add_argument("--dim_corr", type=int, default=192, required=False)
    parser.add_argument("--dim_corr_coarse", type=int, default=64, required=False)
    # parser.add_argument("--dim_corr_all", type=int, default=192, required=False)
    parser.add_argument("--dim_corr_all", type=int, default=256, required=False)
    parser.add_argument("--model", type=str, default="./model/best_twins_ms.pth", required=False)
    parser.add_argument("--fnet", type=str, default='twins', required=False)
    parser.add_argument("--twoscale", type=str, default=True, required=False)

    args = parser.parse_known_args()[0]
    return args

def get_demo_args():

    parser = configargparse.ArgParser(config_file_parser_class=configargparse.YAMLConfigFileParser)
    parser.add_argument('--iters', type=int, default=12)
    parser.add_argument('--mixed_precision', type=bool, default=True)
    parser.add_argument('--small', action='store_true', help='use small model')
    parser.add_argument('--model', type=str, default="./model/pretrain.pth", help="choose the trained model")
    parser.add_argument('--movie_start_idx', type=int, default=2017)
    parser.add_argument('--video_start_idx', type=int, default=0)
    parser.add_argument('--frame_number', type=int, default=304)
    parser.add_argument('--output', type=str, default="output")
    parser.add_argument('--data_path', type=str, default="./demo/data/")

    args = parser.parse_known_args()[0]
    return args