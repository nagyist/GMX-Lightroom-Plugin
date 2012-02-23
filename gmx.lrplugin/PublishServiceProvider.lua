return {
    supportsIncrementalPublish = 'only',
    small_icon = 'gmx-logo.png',
    showSections = {
        'fileNaming',
        'fileSettings',
        'imageSettings',
        'outputSharpening',
        'metatdata',
        'watermarking',
    },
    allowFileFormats = {
        'JPEG',
    },
    allowColorSpaces = {
        'sRGB',
    },
    hidePrintResolution = true,
    canExportVideo = false,
    getCollectionBehaviorInfo = function(publishSettings)
        return {
            defaultCollectionName = 'Fotokiste',
            defaultCollectionCanBeDeleted = false,
            canAddCollection = true,
            maxCollectionSetDepth = 0,
        }
    end
}