// src/metal/device.rs
use std::error::Error;
use std::ptr;
use cocoa::base::{id, nil};
use cocoa::foundation::NSUInteger;
use metal::{MTLDevice, MTLFeatureSet};

pub fn create_device() -> Result<MTLDevice, Box<dyn Error>> {
    let system = unsafe { cocoa::base::class("NSWorkspace") };
    let shared_workspace = unsafe { msg_send![system, sharedWorkspace] };
    
    let screen = unsafe { msg_send![shared_workspace, mainScreen] };
    let screen_rect = unsafe { msg_send![screen, frame] };
    
    // Get default Metal device
    let device = metal::Device::default()
        .ok_or_else(|| "No Metal-compatible GPU found")?;
    
    // Verify device supports required feature set
    let features = device.supports_feature_set(MTLFeatureSet::macOS_GPUFamily1_v1);
    if !features {
        return Err("GPU does not support required Metal features".into());
    }
    
    Ok(device)
}