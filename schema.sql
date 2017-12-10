CREATE DATABASE `whatif`;
SET NAMES utf8mb4;

USE `whatif`;

#  suite 信息表
CREATE TABLE `suite` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `suite_title` varchar(100) NOT NULL DEFAULT '""' COMMENT 'suite标题',
  `suite_source` tinyint(2) NOT NULL DEFAULT '0' COMMENT 'suite来源 0: "unknown", 1: "web", 2: "excel", 3: "log", 4: "xml"',
  `suite_source_name` varchar(100) NOT NULL DEFAULT '""' COMMENT 'suite来源名称',
  `creator` varchar(50) NOT NULL DEFAULT '""' COMMENT '创建人',
  `retry_times` int(10) NOT NULL DEFAULT '0' COMMENT '重试次数',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


#  case 信息表
CREATE TABLE `cases` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `suite_id` int(10) NOT NULL DEFAULT '0' COMMENT '对应suite表的id',
  `title` varchar(100) NOT NULL DEFAULT '""' COMMENT 'case title',
  `request_type` tinyint(3) NOT NULL DEFAULT '0' COMMENT '请求类型 1:  "http", 2: "dubbo Hessian"',
  `request_type_name` varchar(30) NOT NULL DEFAULT '""' COMMENT 'request type 名称',
  `method` tinyint(3) NOT NULL DEFAULT '0' COMMENT '请求方式 1: "get", 2: "post form", 3: "post raw"',
  `method_name` varchar(30) NOT NULL DEFAULT '""' COMMENT 'method 名称',
  `request_url` varchar(500) NOT NULL COMMENT '请求的url',
  `request_body` text COMMENT '请求的body',
  `expect_response` varchar(500) NOT NULL COMMENT '预期返回',
  `expect_time` int(10) NOT NULL COMMENT '预期时间',
  `case_status` tinyint(3) NOT NULL COMMENT '执行结果 0:  "无效", 1: "有效"',
  `case_status_name` varchar(30) NOT NULL DEFAULT '""' COMMENT 'case_status 名称',
  `retry_times` int(10) NOT NULL DEFAULT '0' COMMENT '重试次数',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `tag_list` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(100) NOT NULL DEFAULT '""' COMMENT 'TAG名称',
  `tag_status` tinyint(3) NOT NULL DEFAULT 0 COMMENT 'TAG状态 0:  "无效", 1: "有效"',
  `tag_status_name` varchar(100) NOT NULL DEFAULT '""' COMMENT 'TAG状态名称',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `case_tag` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `case_id` int(10) NOT NULL DEFAULT 0 COMMENT 'case id',
  `tag_id` int(10) NOT NULL DEFAULT 0 COMMENT 'tag id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


#  task 信息表
CREATE TABLE `task` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `suite_id` int(10) NOT NULL DEFAULT 0 COMMENT 'suite id',
  `tags` varchar(500) NOT NULL DEFAULT '""' COMMENT '执行的标签',
  `task_status` int(10) NOT NULL DEFAULT 0 COMMENT '任务状态 0: "未开始", 1: "进行中", 2: "执行成功", 3: "执行失败", 4: "执行中断"',
  `task_status_name` varchar(50) NOT NULL DEFAULT '""' COMMENT '任务状态名称',
  `case_number` int(10) NOT NULL DEFAULT 0 COMMENT '需要执行的case总数',
  `fail_number` int(10) NOT NULL DEFAULT 0 COMMENT '失败的case总数',
  `start_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '开始时间',
  `end_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '结束时间',
  `duration` int(10) NOT NULL DEFAULT 0 COMMENT '持续时间（ms）',
  `creator` varchar(50) NOT NULL DEFAULT '""' COMMENT '创建人',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


#  case执行结果表
CREATE TABLE `task` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `task_id` int(10) NOT NULL DEFAULT 0 COMMENT 'task id',
  `case_id` int(10) NOT NULL DEFAULT 0 COMMENT 'case id',
  `actual_result` text COMMENT '实际结果',
  `retry_time`int(10) NOT NULL DEFAULT 0 COMMENT '重试次数',
  `result_status` int(10) NOT NULL DEFAULT 0 COMMENT '结果 0: "未开始", 1: "进行中", 2: "执行成功", 3: "执行失败", 4: "执行中断"',
  `result_status_name` varchar(50) NOT NULL DEFAULT '""' COMMENT '结果名称',
  `fail_reason ` text COMMENT '失败原因',
  `duration` int(10) NOT NULL DEFAULT 0 COMMENT '持续时间（ms）',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


# 用户信息表
CREATE TABLE `user_info` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) NOT NULL DEFAULT '""' COMMENT '用户名称',
  `user_status` tinyint(3) NOT NULL DEFAULT '0' COMMENT '用户状态：0-未生效；1-已生效；2-已禁用；',
  `user_status_name` varchar(100) NOT NULL DEFAULT '""' COMMENT '用户名称',
  `create_time` timestamp NOT NULL DEFAULT '1970-01-02 00:00:00' COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
