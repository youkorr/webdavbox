import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import web_server_base
from esphome.const import (
    CONF_ID,
    CONF_PORT,
    CONF_AUTH,
    CONF_USERNAME,
    CONF_PASSWORD
)
from esphome.core import CORE

DEPENDENCIES = ["esp32", "web_server_base"]
AUTO_LOAD = ["web_server_base"]

webdav_ns = cg.esphome_ns.namespace("webdav")
WebDavComponent = webdav_ns.class_("WebDavBox", cg.Component)

CONF_MOUNT_POINT = "mount_point"
CONF_SD_DAT0_PIN = "sd_dat0_pin"
CONF_SD_DAT1_PIN = "sd_dat1_pin"
CONF_SD_DAT2_PIN = "sd_dat2_pin" 
CONF_SD_DAT3_PIN = "sd_dat3_pin"
CONF_SD_CMD_PIN = "sd_cmd_pin"
CONF_SD_CLK_PIN = "sd_clk_pin"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(WebDavComponent),
    cv.Optional(CONF_PORT, default=80): cv.port,
    cv.Optional(CONF_MOUNT_POINT, default="/webdav"): cv.string,
    cv.Optional(CONF_AUTH, default=True): cv.boolean,
    cv.Optional(CONF_USERNAME, default="admin"): cv.string,
    cv.Optional(CONF_PASSWORD, default="admin"): cv.string,
    cv.Optional(CONF_SD_DAT0_PIN): cv.int_,
    cv.Optional(CONF_SD_DAT1_PIN): cv.int_,
    cv.Optional(CONF_SD_DAT2_PIN): cv.int_,
    cv.Optional(CONF_SD_DAT3_PIN): cv.int_,
    cv.Optional(CONF_SD_CMD_PIN): cv.int_,
    cv.Optional(CONF_SD_CLK_PIN): cv.int_,
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    
    cg.add(var.set_port(config[CONF_PORT]))
    cg.add(var.set_mount_point(config[CONF_MOUNT_POINT]))
    cg.add(var.set_auth_enabled(config[CONF_AUTH]))
    cg.add(var.set_username(config[CONF_USERNAME]))
    cg.add(var.set_password(config[CONF_PASSWORD]))
    
    if CONF_SD_DAT0_PIN in config:
        cg.add(var.set_sd_dat0_pin(config[CONF_SD_DAT0_PIN]))
    if CONF_SD_DAT1_PIN in config:
        cg.add(var.set_sd_dat1_pin(config[CONF_SD_DAT1_PIN]))
    if CONF_SD_DAT2_PIN in config:
        cg.add(var.set_sd_dat2_pin(config[CONF_SD_DAT2_PIN]))
    if CONF_SD_DAT3_PIN in config:
        cg.add(var.set_sd_dat3_pin(config[CONF_SD_DAT3_PIN]))
    if CONF_SD_CMD_PIN in config:
        cg.add(var.set_sd_cmd_pin(config[CONF_SD_CMD_PIN]))
    if CONF_SD_CLK_PIN in config:
        cg.add(var.set_sd_clk_pin(config[CONF_SD_CLK_PIN]))
    
    # Add build flags for ESP-IDF WebDAV dependencies
    cg.add_build_flag("-DWEBDAV_ENABLED=1")
    
    # Add library dependencies
    cg.add_library("HTTPClient", None)
    cg.add_library("FS", None)
    cg.add_library("SD_MMC", None)
