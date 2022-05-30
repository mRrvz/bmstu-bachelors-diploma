
struct block_device {
	sector_t bd_start_sect;
	sector_t bd_nr_sectors;
	struct disk_stats __percpu *bd_stats;
	unsigned long bd_stamp;
	bool bd_read_only;
	dev_t bd_dev;
	int bd_openers;
	struct inode *bd_inode;
	struct super_block *bd_super;
	void *bd_claiming;
	struct device bd_device;
	void *bd_holder;
	int bd_holders;
	bool bd_write_holder;
	struct kobject *bd_holder_dir;
	u8 bd_partno;
	spinlock_t bd_size_lock
	struct gendisk *bd_disk;
	struct request_queue *bd_queue;

	int bd_fsfreeze_count;
	struct mutex bd_fsfreeze_mutex;
	struct super_block *bd_fsfreeze_sb;

	struct partition_meta_info *bd_meta_info;
} __randomize_layout;
