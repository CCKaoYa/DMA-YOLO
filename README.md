# DMA-YOLO
Paper Title:
	A UAV Image Object Detection Algorithm Based on Deep Diverse Branch Block and Multi-scale Auxiliary Feature

Environment Configuration:
	The experimental training epochs are set to 300, with 4 data-loading threads. The optimizer is SGD, and the input image size is fixed at 640×640. A batch size of 8 is used. A linear learning rate scheduling strategy is employed, with the initial learning rate set to 0.01 and the final learning rate set to 0.05. The momentum is set to 0.937.
	Additionally, an early stopping mechanism is implemented with a patience parameter of 50. If no significant improvement in validation accuracy is observed for 50 consecutive epochs, the training process is automatically terminated.
	To enhance the model’s robustness to the complexities of UAV-captured imagery, a comprehensive data augmentation strategy is applied during training, including Mosaic augmentation, random horizontal flipping, random rotation (±20°), color jittering, and random cropping. These operations increase the diversity of training samples and improve the model’s generalization capability in real-world aerial object detection scenarios.

Code Availability:
	We currently provide a partial release of the source code. The complete codebase will be made publicly available upon publication of the paper. If you urgently need access to the full implementation, please feel free to contact us via email: Wangwf@nit.edu.cn.
