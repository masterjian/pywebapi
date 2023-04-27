/*
 注意，这不是一个非常规范的数据集

 Source Server         : niit-master
 Source Server Type    : MySQL
 Source Server Version : 50733 (5.7.33-log)
 Source Host           : niit-master:3306
 Source Schema         : sem7

 Target Server Type    : MySQL
 Target Server Version : 50733 (5.7.33-log)
 File Encoding         : 65001

 Date: 03/12/2022 21:01:55
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `studentid` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '学号',
  `studentname` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '姓名',
  `batchno` int(11) NULL DEFAULT NULL COMMENT '原班级',
  `new_batchno` int(11) NULL DEFAULT NULL COMMENT '实训班级',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '实训学生管理' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of students
-- ----------------------------
INSERT INTO `students` VALUES (1, '2020040031', 'zhangsan', 1, 2);
INSERT INTO `students` VALUES (2, '1212', '11111', 1, 2);
INSERT INTO `students` VALUES (3, '123456', 'lisisi', 1234, 4321);
INSERT INTO `students` VALUES (4, '123456', '李四', 444, 666);
INSERT INTO `students` VALUES (5, NULL, '张三', NULL, NULL);
INSERT INTO `students` VALUES (6, NULL, '李四', NULL, NULL);
INSERT INTO `students` VALUES (7, NULL, '李四', NULL, NULL);
INSERT INTO `students` VALUES (8, NULL, 'zhangsan', NULL, NULL);
INSERT INTO `students` VALUES (9, NULL, '李四', NULL, NULL);
INSERT INTO `students` VALUES (10, NULL, 'zhangsan', NULL, NULL);
INSERT INTO `students` VALUES (11, NULL, '李四', NULL, NULL);
INSERT INTO `students` VALUES (12, NULL, 'zhangsan', NULL, NULL);
INSERT INTO `students` VALUES (13, NULL, '李四', NULL, NULL);
INSERT INTO `students` VALUES (14, NULL, 'zhangsan', NULL, NULL);
INSERT INTO `students` VALUES (15, NULL, '李四', NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
