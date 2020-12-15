from pathlib import Path


GRAPH_ITEM_DIR = f'{str(Path.home())}/graph_items'
SIMULATION_DATA_DIR = f'{str(Path.home())}/autosync_dataset_release'
CHECKPOINT_DIR =  f'{str(Path.home())}'


simulation_params = {
	'ncf_large_adam_dense': {
		'model_batch_size': 256,
		'model_seq_len': 1,
		'data_dir': [
			f'{SIMULATION_DATA_DIR}/cluster1/ncf_large_adam_dense_g3.4.25.1',
			f'{SIMULATION_DATA_DIR}/cluster1/ncf_large_adam_dense_g3.4.25.1_g3.4.25.2',
			f'{SIMULATION_DATA_DIR}/cluster1/ncf_large_adam_dense_g3.4.25.1_g3.4.25.2_2',
			f'{SIMULATION_DATA_DIR}/cluster1/ncf_large_adam_dense_g3.4.25.1_g3.4.25.2_g3.4.25.3_g3.4.25.4_3.4.25.6_g3.4.25.7_g3.4.25.8_g3.4.25.9',
			f'{SIMULATION_DATA_DIR}/cluster1/ncf_large_adam_dense_g3.4.25.6_g3.4.25.7_g3.4.25.8_g3.4.25.9',
        ],
		'original_graph_item_path': f'{GRAPH_ITEM_DIR}/ncf_original_graph_item',
        'save_dir': f'{CHECKPOINT_DIR}/ncf_predefined_checkpoints',
		'save_prefix': 'ckpV1_ncf_large_adam_dense',
		'baseline': 0.15,
		'scale': 0.5,
		'learning_rate': 0.01,
		'list_size': 2,
		'batch_size': 100,
		'ranking_loss_key': 'pairwise_logistic_loss',
		'model_version': 'v1',
		'do_train': False,
		'do_test': True,
		'checkpoint': f'{CHECKPOINT_DIR}/ncf/predefined_checkpoints/ckpV1_ncf_large_adam_dense_orca_all_600_0.83249_0.84517',
	},
	'bert': {
		'model_batch_size': 32,
		'model_seq_len': 128,
		'data_dir': [
			f'{SIMULATION_DATA_DIR}/cluster2/bert_large_random_orca_11',
			f'{SIMULATION_DATA_DIR}/cluster2/bert_large_orca_11_random_rej-13_trial-100-_expolre-3000_model-on-bert-orca_embedding_sim-weight-0.3_max-par-20_if-partition-lb-100000-zhijie',
			f'{SIMULATION_DATA_DIR}/cluster2/bert_large_orca_11_test_run',
			f'{SIMULATION_DATA_DIR}/cluster2/bert_large_orca_11_random_rej-3.5_trial-50_expolre-1000_model-new-2_embedding_sim-1.0',
			f'{SIMULATION_DATA_DIR}/cluster2/bert_large_orca_11_random_rej-8_trial-30_expolre-1000_model-new-3_embedding_sim-0.2_ps-only',
			f'{SIMULATION_DATA_DIR}/cluster2/bert_large_orca_11_random_rej-8_trial-50_expolre-1000_model-new-3_embedding_sim-0.4_ps-only',
			f'{SIMULATION_DATA_DIR}/cluster2/bert_large_orca_11_random_rej-13_trial-20-_expolre-100_model-on-bert-orca_embedding_sim-weight-0.3_max-par-20_if-partition-lb-100000',
			f'{SIMULATION_DATA_DIR}/bert/bert-aws/bert-large-aws4g4',
			f'{SIMULATION_DATA_DIR}/bert/bert-aws/bert_large_random_search_aws_4_ps_only',
		],
        'original_graph_item_path': f'{GRAPH_ITEM_DIR}/bert_original_graph_item_large',
        'save_dir': f'{CHECKPOINT_DIR}/bert_predefined_checkpoints',
		'save_prefix': 'ckpV1_bert_orca',
		'baseline': 0.04,
		'scale': 0.5,
		'learning_rate': 0.01,
		'list_size': 2,
		'batch_size': 100,
		'ranking_loss_key': 'pairwise_logistic_loss',
		'do_train': True,
		'do_test': True,
		'model_version': 'v1',
		'checkpoint': f'{CHECKPOINT_DIR}//bert_predefined_checkpoints/ckpV1_bert_orca_100_0.67000_0.50000',
	},
	'vgg16': {
		'model_batch_size': 32,
		'model_seq_len': 1,
		'data_dir': [
			f'{SIMULATION_DATA_DIR}/cluster1/vgg16_aws4_from_vgg16-orca2aws-421_explore3000',
			f'{SIMULATION_DATA_DIR}/cluster1/vgg16_aws-4_model-aws-new_rejection-4_explore-3000_sim-weight-0.75',
			f'{SIMULATION_DATA_DIR}/cluster1/vgg16_aws-4_model-aws-only_rejection-8_explore-3000_sim-weight-0.3',
			f'{SIMULATION_DATA_DIR}/cluster1/vgg16_aws_4_pure_random',
		],
		'original_graph_item_path': f'{GRAPH_ITEM_DIR}/vgg16_original_graph_item',
		'save_dir': f'{CHECKPOINT_DIR}/vgg16_predefined_checkpoints',
		'save_prefix': 'ckpV1_vgg_aws',
		'baseline': 0.0,
		'scale': 0.5,
		'do_train': True,
		'do_test': True,
		'model_version': 'v1',
		'learning_rate': 0.01,
		'list_size': 2,
		'batch_size': 100,
		'ranking_loss_key': 'pairwise_logistic_loss',
		'checkpoint': '',
	},
	'resnet101': {
		'model_batch_size': 32,
		'model_seq_len': 1,
		'baseline': 0.5,
		'scale': 0.5,
		'data_dir': '',
		'learning_rate': 0.01,
		'list_size': 2,
		'batch_size': 100,
		'ranking_loss_key': 'pairwise_logistic_loss',
	},
}