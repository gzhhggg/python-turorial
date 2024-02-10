from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `admins` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `username` VARCHAR(50) NOT NULL UNIQUE,
    `password` VARCHAR(200) NOT NULL,
    `last_login` DATETIME(6) NOT NULL  COMMENT 'Last Login',
    `email` VARCHAR(200) NOT NULL  DEFAULT '',
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `clients` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `members` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `phone` VARCHAR(255) NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6),
    `client_id` BIGINT NOT NULL,
    CONSTRAINT `fk_members_clients_a49ec662` FOREIGN KEY (`client_id`) REFERENCES `clients` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `member_costs` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `start_date` DATE NOT NULL,
    `end_date` DATE,
    `cost` INT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6),
    `member_id` BIGINT NOT NULL,
    CONSTRAINT `fk_member_c_members_af24c34e` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `projects` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `start_date` DATE NOT NULL,
    `end_date` DATE,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6),
    `client_id` BIGINT NOT NULL,
    CONSTRAINT `fk_projects_clients_52105678` FOREIGN KEY (`client_id`) REFERENCES `clients` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `project_budgets` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `start_date` DATE NOT NULL,
    `end_date` DATE,
    `budget` INT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6),
    `project_id` BIGINT NOT NULL,
    CONSTRAINT `fk_project__projects_35b2b234` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `project_slots` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `start_date` DATE NOT NULL,
    `end_date` DATE,
    `budget` INT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6),
    `project_id` BIGINT NOT NULL,
    CONSTRAINT `fk_project__projects_d4627048` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `project_member_assigns` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `start_date` DATE NOT NULL,
    `end_date` DATE,
    `cost` INT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6),
    `member_id` BIGINT NOT NULL,
    `project_slot_id` BIGINT NOT NULL,
    CONSTRAINT `fk_project__members_29a1f08f` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_project__project__b6376f95` FOREIGN KEY (`project_slot_id`) REFERENCES `project_slots` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
