from .variables import BaseVariable

class BaseBlock:
    blockType = ""
    blockAction = ""
    def __init__(self, *args:BaseVariable):
        self.args = args
    def export(self) -> list:
        items = []
        slot = 0
        for arg in self.args:
            earg = arg.export(slot)
            items.append(earg)
            slot =+ slot
        return [
            {
                "id": "block",
                "block": self.blockType,
                "args": {
                    "items": items
                },
                "action": self.blockAction
            }
        ]

class BaseBracketedBlock(BaseBlock):
    bracketType = "norm"
    def __init__(self, *args: BaseVariable):
        super().__init__(*args)
        self.blocks = []
    def add_block(self, block:BaseBlock):
        self.blocks.append(block)
    def remove_block(self, id:int):
        self.blocks.pop(id)
    def export(self) -> list:
        start_block = super().export()[0]
        eblocks = [start_block]
        eblocks.append({
            "id": "bracket",
            "type": "norm",
            "direct": "open"
        })
        for block in self.blocks:
            eblock = block.export()
            for eb in eblock:
                eblocks.append(eb)
        eblocks.append({
            "id": "bracket",
            "type": self.bracketType,
            "direct": "close"
        })
        return eblocks

####################################
#           PLAYER EVENT           #
####################################

class PlayerEvent(BaseBlock):
    blockType = "event"

# Plot and server events

class PlayerEvent_Join(PlayerEvent):
    blockAction = "Join"

class PlayerEvent_Leave(PlayerEvent):
    blockAction = "Leave"

class PlayerEvent_Command(PlayerEvent):
    blockAction = "Command"

# Click events

class PlayerEvent_RightClick(PlayerEvent):
    blockAction = "RightClick"

class PlayerEvent_LeftClick(PlayerEvent):
    blockAction = "LeftClick"

class PlayerEvent_ClickEntity(PlayerEvent):
    blockAction = "ClickEntity"

class PlayerEvent_ClickPlayer(PlayerEvent):
    blockAction = "ClickPlayer"

class PlayerEvent_PlaceBlock(PlayerEvent):
    blockAction = "PlaceBlock"

class PlayerEvent_BreakBlock(PlayerEvent):
    blockAction = "BreakBlock"

class PlayerEvent_SwapHands(PlayerEvent):
    blockAction = "SwapHands"

class PlayerEvent_ChangeSlow(PlayerEvent):
    blockAction = "ChangeSlow"

class PlayerEvent_TameEntity(PlayerEvent):
    blockAction = "TameEntity"

# Movement events

class PlayerEvent_Walk(PlayerEvent):
    blockAction = "Walk"

class PlayerEvent_Jump(PlayerEvent):
    blockAction = "Jump"

class PlayerEvent_Sneak(PlayerEvent):
    blockAction = "Sneak"

class PlayerEvent_Unsneak(PlayerEvent):
    blockAction = "Unsneak"

class PlayerEvent_StartSprint(PlayerEvent):
    blockAction = "StartSprint"

class PlayerEvent_StopSprint(PlayerEvent):
    blockAction = "StopSprint"

class PlayerEvent_StartFly(PlayerEvent):
    blockAction = "StartFly"

class PlayerEvent_StopFly(PlayerEvent):
    blockAction = "StopFly"

class PlayerEvent_Riptide(PlayerEvent):
    blockAction = "Riptide"

class PlayerEvent_Dismount(PlayerEvent):
    blockAction = "Dismount"

class PlayerEvent_HorseJump(PlayerEvent):
    blockAction = "HorseJump"

class PlayerEvent_VehicleJump(PlayerEvent):
    blockAction = "VehicleJump"

# Item events

class PlayerEvent_ClickMenuSlot(PlayerEvent):
    blockAction = "ClickMenuSlot"

class PlayerEvent_ClickInv(PlayerEvent):
    blockAction = "ClickInv"

class PlayerEvent_ClickCraftSlot(PlayerEvent):
    blockAction = "ClickCraftSlot"

class PlayerEvent_PickUpItem(PlayerEvent):
    blockAction = "PickUpItem"

class PlayerEvent_DropItem(PlayerEvent):
    blockAction = "DropItem"

class PlayerEvent_Consume(PlayerEvent):
    blockAction = "Consume"

class PlayerEvent_BreakItem(PlayerEvent):
    blockAction = "BreakItem"

class PlayerEvent_CloseInv(PlayerEvent):
    blockAction = "CloseInv"

class PlayerEvent_Fish(PlayerEvent):
    blockAction = "Fish"

# Damage events

class PlayerEvent_PlayerTakeDmg(PlayerEvent):
    blockAction = "PlayerTakeDmg"

class PlayerEvent_PlayerDmgPlayer(PlayerEvent):
    blockAction = "PlayerDmgPlayer"

class PlayerEvent_DamageEntity(PlayerEvent):
    blockAction = "DamageEntity"

class PlayerEvent_EntityDmgPlayer(PlayerEvent):
    blockAction = "EntityDmgPlayer"

class PlayerEvent_PlayerHeal(PlayerEvent):
    blockAction = "PlayerHeal"

class PlayerEvent_ShootBow(PlayerEvent):
    blockAction = "ShootBow"

class PlayerEvent_ShootProjectile(PlayerEvent):
    blockAction = "ShootProjectile"

class PlayerEvent_ProjHit(PlayerEvent):
    blockAction = "ProjHit"

class PlayerEvent_ProjDmgPlayer(PlayerEvent):
    blockAction = "ProjDmgPlayer"

class PlayerEvent_CloudImbuePlayer(PlayerEvent):
    blockAction = "CloudImbuePlayer"

# Death events

class PlayerEvent_Death(PlayerEvent):
    blockAction = "Death"

class PlayerEvent_KillPlayer(PlayerEvent):
    blockAction = "KillPlayer"

class PlayerEvent_PlayerResurrect(PlayerEvent):
    blockAction = "PlayerResurrect"

class PlayerEvent_KillMob(PlayerEvent):
    blockAction = "KillMob"

class PlayerEvent_MobKillPlayer(PlayerEvent):
    blockAction = "MobKillPlayer"

class PlayerEvent_Respawn(PlayerEvent):
    blockAction = "Respawn"

####################################
#           PLAYER ACTION          #
####################################

class PlayerAction(BaseBlock):
    blockType = "player_action"

# Item managment

class PlayerAction_GiveItems(PlayerAction):
    blockAction = "GiveItems"

class PlayerAction_SetHotbar(PlayerAction):
    blockAction = "SetHotbar"

class PlayerAction_SetInventory(PlayerAction):
    blockAction = "SetInventory"

class PlayerAction_SetSlotItem(PlayerAction):
    blockAction = "SetSlotItem"

class PlayerAction_SetEquipment(PlayerAction):
    blockAction = "SetEquipment"

class PlayerAction_SetArmor(PlayerAction):
    blockAction = "SetArmor"

class PlayerAction_ReplaceItems(PlayerAction):
    blockAction = "ReplaceItems"

class PlayerAction_RemoveItems(PlayerAction):
    blockAction = "RemoveItems"

class PlayerAction_ClearItems(PlayerAction):
    blockAction = "ClearItems"

class PlayerAction_ClearInv(PlayerAction):
    blockAction = "ClearInv"

class PlayerAction_SetCursorItem(PlayerAction):
    blockAction = "SetCursorItem"

class PlayerAction_SaveInv(PlayerAction):
    blockAction = "SaveInv"

class PlayerAction_LoadInv(PlayerAction):
    blockAction = "LoadInv"

class PlayerAction_SetItemCooldown(PlayerAction):
    blockAction = "SetItemCooldown"

# Communication

class PlayerAction_SendMessage(PlayerAction):
    blockAction = "SendMessage"

class PlayerAction_SendMessageSeq(PlayerAction):
    blockAction = "SendMessageSeq"

class PlayerAction_SendHover(PlayerAction):
    blockAction = "SendHover"

class PlayerAction_SendTitle(PlayerAction):
    blockAction = "SendTitle"

class PlayerAction_ActionBar(PlayerAction):
    blockAction = "ActionBar"

class PlayerAction_OpenBook(PlayerAction):
    blockAction = "OpenBook"

class PlayerAction_SetBossBar(PlayerAction):
    blockAction = "SetBossBar"

class PlayerAction_RemoveBossBar(PlayerAction):
    blockAction = "RemoveBossBar"

class PlayerAction_SendAdvancement(PlayerAction):
    blockAction = "SendAdvancement"

class PlayerAction_SetTabListInfo(PlayerAction):
    blockAction = "SetTabListInfo"

class PlayerAction_PlaySound(PlayerAction):
    blockAction = "PlaySound"

class PlayerAction_StopSound(PlayerAction):
    blockAction = "StopSound"

class PlayerAction_PlaySoundSeq(PlayerAction):
    blockAction = "PlaySoundSeq"

class PlayerAction_PlayEntitySound(PlayerAction):
    blockAction = "PlayEntitySound"

# Inventory Menus

class PlayerAction_ShowInv(PlayerAction):
    blockAction = "ShowInv"

class PlayerAction_ExpandInv(PlayerAction):
    blockAction = "ExpandInv"

class PlayerAction_SetMenuItem(PlayerAction):
    blockAction = "SetMenuItem"

class PlayerAction_SetInvName(PlayerAction):
    blockAction = "SetInvName"

class PlayerAction_AddInvRow(PlayerAction):
    blockAction = "AddInvRow"

class PlayerAction_RemoveInvRow(PlayerAction):
    blockAction = "RemoveInvRow"

class PlayerAction_CloseInv(PlayerAction):
    blockAction = "CloseInv"

class PlayerAction_OpenBlockInv(PlayerAction):
    blockAction = "OpenBlockInv"

class PlayerAction_SetCraftResult(PlayerAction):
    blockAction = "SetCraftResult"

class PlayerAction_SetCraftingItem(PlayerAction):
    blockAction = "SetCraftingItem"

class PlayerAction_SetCraftingItems(PlayerAction):
    blockAction = "SetCraftingItems"

# Scoreboard manipulation

class PlayerAction_SetScoreObj(PlayerAction):
    blockAction = "SetScoreObj"

class PlayerAction_SetSidebar(PlayerAction):
    blockAction = "SetSidebar"

class PlayerAction_SetScore(PlayerAction):
    blockAction = "SetScore"

class PlayerAction_RemoveScore(PlayerAction):
    blockAction = "RemoveScore"

class PlayerAction_ClearScoreboard(PlayerAction):
    blockAction = "ClearScoreboard"

# Statistics

class PlayerAction_Damage(PlayerAction):
    blockAction = "Damage"

class PlayerAction_Heal(PlayerAction):
    blockAction = "Heal"

class PlayerAction_SetHealth(PlayerAction):
    blockAction = "SetHealth"

class PlayerAction_SetMaxHealth(PlayerAction):
    blockAction = "SetMaxHealth"

class PlayerAction_SetAbsorption(PlayerAction):
    blockAction = "SetAbsorption"

class PlayerAction_SetFoodLevel(PlayerAction):
    blockAction = "SetFoodLevel"

class PlayerAction_SetSaturation(PlayerAction):
    blockAction = "SetSaturation"

class PlayerAction_GiveExp(PlayerAction):
    blockAction = "GiveExp"

class PlayerAction_SetExp(PlayerAction):
    blockAction = "SetExp"

class PlayerAction_GivePotion(PlayerAction):
    blockAction = "GivePotion"

class PlayerAction_RemovePotion(PlayerAction):
    blockAction = "RemovePotion"

class PlayerAction_ClearPotions(PlayerAction):
    blockAction = "ClearPotions"

class PlayerAction_SetSlot(PlayerAction):
    blockAction = "SetSlot"

class PlayerAction_SetAtkSpeed(PlayerAction):
    blockAction = "SetAtkSpeed"

class PlayerAction_SetFireTicks(PlayerAction):
    blockAction = "SetFireTicks"

class PlayerAction_SetFreezeTicks(PlayerAction):
    blockAction = "SetFreezeTicks"

class PlayerAction_SetAirTicks(PlayerAction):
    blockAction = "SetAirTicks"

class PlayerAction_SetInvulTicks(PlayerAction):
    blockAction = "SetInvulTicks"

class PlayerAction_SetFallDistance(PlayerAction):
    blockAction = "SetFallDistance"

class PlayerAction_SetSpeed(PlayerAction):
    blockAction = "SetSpeed"

# Settings

class PlayerAction_SurvivalMode(PlayerAction):
    blockAction = "SurvivalMode"

class PlayerAction_AdventureMode(PlayerAction):
    blockAction = "AdventureMode"

class PlayerAction_CreativeMode(PlayerAction):
    blockAction = "CreativeMode"

class PlayerAction_SpectatorMode(PlayerAction):
    blockAction = "SpectatorMode"

class PlayerAction_SetAllowFlight(PlayerAction):
    blockAction = "SetAllowFlight"

class PlayerAction_SetAllowPVP(PlayerAction):
    blockAction = "SetAllowPVP"

class PlayerAction_SetDropsEnabled(PlayerAction):
    blockAction = "SetDropsEnabled"

class PlayerAction_SetInventoryKept(PlayerAction):
    blockAction = "SetInventoryKept"

class PlayerAction_SetCollidable(PlayerAction):
    blockAction = "SetCollidable"

class PlayerAction_EnableBlocks(PlayerAction):
    blockAction = "EnableBlocks"

class PlayerAction_DisableBlocks(PlayerAction):
    blockAction = "DisableBlocks"

class PlayerAction_InstantRespawn(PlayerAction):
    blockAction = "InstantRespawn"

class PlayerAction_SetReducedDebug(PlayerAction):
    blockAction = "SetReducedDebug"

# Movement

class PlayerAction_Teleport(PlayerAction):
    blockAction = "Teleport"

class PlayerAction_LaunchUp(PlayerAction):
    blockAction = "LaunchUp"

class PlayerAction_LaunchFwd(PlayerAction):
    blockAction = "LaunchFwd"

class PlayerAction_LaunchToward(PlayerAction):
    blockAction = "LaunchToward"

class PlayerAction_RideEntity(PlayerAction):
    blockAction = "RideEntity"

class PlayerAction_SetFlying(PlayerAction):
    blockAction = "SetFlying"

class PlayerAction_SetGliding(PlayerAction):
    blockAction = "SetGliding"

class PlayerAction_BoostElytra(PlayerAction):
    blockAction = "BoostElytra"

class PlayerAction_SetRotation(PlayerAction):
    blockAction = "SetRotation"

class PlayerAction_FaceLocation(PlayerAction):
    blockAction = "FaceLocation"

class PlayerAction_SetVelocity(PlayerAction):
    blockAction = "SetVelocity"

class PlayerAction_SpectateTarget(PlayerAction):
    blockAction = "SpectateTarget"

class PlayerAction_SetSpawnPoint(PlayerAction):
    blockAction = "SetSpawnPoint"

# World

class PlayerAction_LaunchProj(PlayerAction):
    blockAction = "LaunchProj"

class PlayerAction_SetPlayerTime(PlayerAction):
    blockAction = "SetPlayerTime"

class PlayerAction_SetPlayerWeather(PlayerAction):
    blockAction = "SetPlayerWeather"

class PlayerAction_SetCompass(PlayerAction):
    blockAction = "SetCompass"

class PlayerAction_DisplayBlock(PlayerAction):
    blockAction = "DisplayBlock"

class PlayerAction_DisplayFracture(PlayerAction):
    blockAction = "DisplayFracture"

class PlayerAction_DisplayBlockOpen(PlayerAction):
    blockAction = "DisplayBlockOpen"

class PlayerAction_DisplayGateway(PlayerAction):
    blockAction = "DisplayGateway"

class PlayerAction_DisplaySignText(PlayerAction):
    blockAction = "DisplaySignText"

class PlayerAction_DisplayHologram(PlayerAction):
    blockAction = "DisplayHologram"

class PlayerAction_SetFogDistance(PlayerAction):
    blockAction = "SetFogDistance"

class PlayerAction_SetWorldBorder(PlayerAction):
    blockAction = "SetWorldBorder"

class PlayerAction_ShiftWorldBorder(PlayerAction):
    blockAction = "ShiftWorldBorder"

class PlayerAction_RmWorldBorder(PlayerAction):
    blockAction = "RmWorldBorder"

class PlayerAction_DisplayPickup(PlayerAction):
    blockAction = "DisplayPickup"

class PlayerAction_SetEntityHidden(PlayerAction):
    blockAction = "SetEntityHidden"

# Visual effects

class PlayerAction_Particle(PlayerAction):
    blockAction = "Particle"

class PlayerAction_ParticleLine(PlayerAction):
    blockAction = "ParticleLine"

class PlayerAction_ParticleLineA(PlayerAction):
    blockAction = "ParticleLineA"

class PlayerAction_ParticleCircle(PlayerAction):
    blockAction = "ParticleCircle"

class PlayerAction_ParticleCircleA(PlayerAction):
    blockAction = "ParticleCircleA"

class PlayerAction_ParticleCuboid(PlayerAction):
    blockAction = "ParticleCuboid"

class PlayerAction_ParticleCuboidA(PlayerAction):
    blockAction = "ParticleCuboidA"

class PlayerAction_ParticleSpiral(PlayerAction):
    blockAction = "ParticleSpiral"

class PlayerAction_ParticleSpiralA(PlayerAction):
    blockAction = "ParticleSpiralA"

class PlayerAction_ParticleSphere(PlayerAction):
    blockAction = "ParticleSphere"

class PlayerAction_ParticleRay(PlayerAction):
    blockAction = "ParticleRay"

class PlayerAction_DisplayLightning(PlayerAction):
    blockAction = "DisplayLightning"

class PlayerAction_Vibration(PlayerAction):
    blockAction = "Vibration"

# Appearance

class PlayerAction_MobDisguise(PlayerAction):
    blockAction = "MobDisguise"

class PlayerAction_PlayerDisguise(PlayerAction):
    blockAction = "PlayerDisguise"

class PlayerAction_BlockDisguise(PlayerAction):
    blockAction = "BlockDisguise"

class PlayerAction_SetDisguiseVisible(PlayerAction):
    blockAction = "SetDisguiseVisible"

class PlayerAction_Undisguise(PlayerAction):
    blockAction = "Undisguise"

class PlayerAction_SetChatTag(PlayerAction):
    blockAction = "SetChatTag"

class PlayerAction_ChatColor(PlayerAction):
    blockAction = "ChatColor"

class PlayerAction_SetNameColor(PlayerAction):
    blockAction = "SetNameColor"

class PlayerAction_SetArrowsStuck(PlayerAction):
    blockAction = "SetArrowsStuck"

class PlayerAction_SetStingsStuck(PlayerAction):
    blockAction = "SetStingsStuck"

class PlayerAction_SetVisualFire(PlayerAction):
    blockAction = "SetVisualFire"

class PlayerAction_AttackAnimation(PlayerAction):
    blockAction = "AttackAnimation"

class PlayerAction_HurtAnimation(PlayerAction):
    blockAction = "HurtAnimation"

class PlayerAction_WakeUpAnimation(PlayerAction):
    blockAction = "WakeUpAnimation"

class PlayerAction_SetStatus(PlayerAction):
    blockAction = "SetStatus"

class PlayerAction_SetSkin(PlayerAction):
    blockAction = "SetSkin"

# Miscellanious

class PlayerAction_RollbackBlocks(PlayerAction):
    blockAction = "RollbackBlocks"

class PlayerAction_Kick(PlayerAction):
    blockAction = "Kick"

####################################
#           SET VARIABLE           #
####################################

class SetVariable(BaseBlock):
    blockType = "set_var"

# Variable setting

class SetVariable_SetValue(SetVariable):
    blockAction = "="

class SetVariable_RandomValue(SetVariable):
    blockAction = "RandomValue"

class SetVariable_PurgeVars(SetVariable):
    blockAction = "PurgeVars"

# Numerical actions

class SetVariable_Add(SetVariable):
    blockAction = "+"

class SetVariable_Subtract(SetVariable):
    blockAction = "-"

class SetVariable_Multiply(SetVariable):
    blockAction = "x"

class SetVariable_Divide(SetVariable):
    blockAction = "/"

class SetVariable_Remainder(SetVariable):
    blockAction = "%"

class SetVariable_Increment(SetVariable):
    blockAction = "+="

class SetVariable_Decrement(SetVariable):
    blockAction = "-="

class SetVariable_Exponent(SetVariable):
    blockAction = "Exponent"

class SetVariable_Root(SetVariable):
    blockAction = "Root"

class SetVariable_Logarithm(SetVariable):
    blockAction = "Logarithm"

class SetVariable_ParseNumber(SetVariable):
    blockAction = "ParseNumber"

class SetVariable_AbsoluteValue(SetVariable):
    blockAction = "AbsoluteValue"

class SetVariable_ClampNumber(SetVariable):
    blockAction = "ClampNumber"

class SetVariable_WrapNumber(SetVariable):
    blockAction = "WrapNumber"

class SetVariable_Average(SetVariable):
    blockAction = "Average"

class SetVariable_RandomNumber(SetVariable):
    blockAction = "RandomNumber"

class SetVariable_RoundNumber(SetVariable):
    blockAction = "RoundNumber"

class SetVariable_MinNumber(SetVariable):
    blockAction = "MinNumber"

class SetVariable_MaxNumber(SetVariable):
    blockAction = "MaxNumber"

class SetVariable_NormalRandom(SetVariable):
    blockAction = "NormalRandom"

class SetVariable_Sine(SetVariable):
    blockAction = "Sine"

class SetVariable_Cosine(SetVariable):
    blockAction = "Cosine"

class SetVariable_Tangent(SetVariable):
    blockAction = "Tangent"

class SetVariable_PerlinNoise(SetVariable):
    blockAction = "PerlinNoise"

class SetVariable_VoroniNoise(SetVariable):
    blockAction = "VoroniNoise"

class SetVariable_WorleyNoise(SetVariable):
    blockAction = "WorleyNoise"

class SetVariable_Bitwise(SetVariable):
    blockAction = "Bitwise"

# Text manipulation

class SetVariable_Text(SetVariable):
    blockAction = "Text"

class SetVariable_ReplaceText(SetVariable):
    blockAction = "ReplaceText"

class SetVariable_RemoveText(SetVariable):
    blockAction = "RemoveText"

class SetVariable_TrimText(SetVariable):
    blockAction = "TrimText"

class SetVariable_SplitText(SetVariable):
    blockAction = "SplitText"

class SetVariable_JoinText(SetVariable):
    blockAction = "JoinText"

class SetVariable_SetCase(SetVariable):
    blockAction = "SetCase"

class SetVariable_TranslateColors(SetVariable):
    blockAction = "TranslateColors"

class SetVariable_TextLength(SetVariable):
    blockAction = "TextLength"

class SetVariable_RepeatText(SetVariable):
    blockAction = "RepeatText"

class SetVariable_FormatTime(SetVariable):
    blockAction = "FormatTime"

# Location manipulation

class SetVariable_GetCoord(SetVariable):
    blockAction = "GetCoord"

class SetVariable_SetCoord(SetVariable):
    blockAction = "SetCoord"

class SetVariable_SetAllCoords(SetVariable):
    blockAction = "SetAllCoords"

class SetVariable_ShiftOnAxis(SetVariable):
    blockAction = "ShiftOnAxis"

class SetVariable_ShiftAllAxis(SetVariable):
    blockAction = "ShiftAllAxis"

class SetVariable_ShiftInDirection(SetVariable):
    blockAction = "ShiftInDirection"

class SetVariable_ShiftAllDirections(SetVariable):
    blockAction = "ShiftAllDirections"

class SetVariable_ShiftToward(SetVariable):
    blockAction = "ShiftToward"

class SetVariable_ShiftOnVector(SetVariable):
    blockAction = "ShiftOnVector"

class SetVariable_GetDirection(SetVariable):
    blockAction = "GetDirection"

class SetVariable_SetDirection(SetVariable):
    blockAction = "SetDirection"

class SetVariable_ShiftRotation(SetVariable):
    blockAction = "ShiftRotation"

class SetVariable_FaceLocation(SetVariable):
    blockAction = "FaceLocation"

class SetVariable_AlignLoc(SetVariable):
    blockAction = "AlignLoc"

class SetVariable_Distance(SetVariable):
    blockAction = "Distance"

class SetVariable_GetCenterLoc(SetVariable):
    blockAction = "GetCenterLoc"

class SetVariable_RandomLoc(SetVariable):
    blockAction = "RandomLoc"

# Item manipulation

class SetVariable_GetItemType(SetVariable):
    blockAction = "GetItemType"

class SetVariable_SetItemType(SetVariable):
    blockAction = "SetItemType"

class SetVariable_GetItemName(SetVariable):
    blockAction = "GetItemName"

class SetVariable_SetItemName(SetVariable):
    blockAction = "SetItemName"

class SetVariable_GetItemLore(SetVariable):
    blockAction = "GetItemLore"

class SetVariable_GetItemLoreLine(SetVariable):
    blockAction = "GetItemLoreLine"

class SetVariable_SetItemLore(SetVariable):
    blockAction = "SetItemLore"

class SetVariable_GetItemAmount(SetVariable):
    blockAction = "GetItemAmount"

class SetVariable_SetItemAmount(SetVariable):
    blockAction = "SetItemAmount"

class SetVariable_GetMaxItemAmount(SetVariable):
    blockAction = "GetMaxItemAmount"

class SetVariable_GetItemDura(SetVariable):
    blockAction = "GetItemDura"

class SetVariable_SetItemDura(SetVariable):
    blockAction = "SetItemDura"

class SetVariable_SetBreakability(SetVariable):
    blockAction = "SetBreakability"

class SetVariable_GetItemEnchants(SetVariable):
    blockAction = "GetItemEnchants"

class SetVariable_SetItemEnchants(SetVariable):
    blockAction = "SetItemEnchants"

class SetVariable_AddItemEnchant(SetVariable):
    blockAction = "AddItemEnchant"

class SetVariable_RemoveItemEnchant(SetVariable):
    blockAction = "RemoveItemEnchant"

class SetVariable_GetHeadOwner(SetVariable):
    blockAction = "GetHeadOwner"

class SetVariable_SetHeadTexture(SetVariable):
    blockAction = "SetHeadTexture"

class SetVariable_GetBookText(SetVariable):
    blockAction = "GetBookText"

class SetVariable_SetBookText(SetVariable):
    blockAction = "SetBookText"

class SetVariable_GetItemTag(SetVariable):
    blockAction = "GetItemTag"

class SetVariable_GetAllItemTags(SetVariable):
    blockAction = "GetAllItemTags"

class SetVariable_SetItemTag(SetVariable):
    blockAction = "SetItemTag"

class SetVariable_RemoveItemTag(SetVariable):
    blockAction = "RemoveItemTag"

class SetVariable_SetModelData(SetVariable):
    blockAction = "SetModelData"

class SetVariable_GetItemEffects(SetVariable):
    blockAction = "GetItemEffects"

class SetVariable_SetItemEffects(SetVariable):
    blockAction = "SetItemEffects"

class SetVariable_SetItemFlags(SetVariable):
    blockAction = "SetItemFlags"

class SetVariable_SetCanPlaceOn(SetVariable):
    blockAction = "SetCanPlaceOn"

class SetVariable_SetCanDestroy(SetVariable):
    blockAction = "SetCanDestroy"

class SetVariable_GetItemRarity(SetVariable):
    blockAction = "GetItemRarity"

class SetVariable_GetLodestoneLoc(SetVariable):
    blockAction = "GetLodestoneLoc"

class SetVariable_SetLodestoneLoc(SetVariable):
    blockAction = "SetLodestoneLoc"

class SetVariable_SetArmorTrim(SetVariable):
    blockAction = "SetArmorTrim"

class SetVariable_GetItemColor(SetVariable):
    blockAction = "GetItemColor"

class SetVariable_SetItemColor(SetVariable):
    blockAction = "SetItemColor"

class SetVariable_GetItemAttribute(SetVariable):
    blockAction = "GetItemAttribute"

class SetVariable_AddItemAttribute(SetVariable):
    blockAction = "AddItemAttribute"

class SetVariable_SetItemTexture(SetVariable):
    blockAction = "SetItemTexture"

# List manipulation

class SetVariable_CreateList(SetVariable):
    blockAction = "CreateList"

class SetVariable_AppendValue(SetVariable):
    blockAction = "AppendValue"

class SetVariable_AppendList(SetVariable):
    blockAction = "AppendList"

class SetVariable_GetListValue(SetVariable):
    blockAction = "GetListValue"

class SetVariable_SetListValue(SetVariable):
    blockAction = "SetListValue"

class SetVariable_GetValueIndex(SetVariable):
    blockAction = "GetValueIndex"

class SetVariable_ListLength(SetVariable):
    blockAction = "ListLength"

class SetVariable_InsertListValue(SetVariable):
    blockAction = "InsertListValue"

class SetVariable_RemoveListValue(SetVariable):
    blockAction = "RemoveListValue"

class SetVariable_RemoveListIndex(SetVariable):
    blockAction = "RemoveListIndex"

class SetVariable_TrimList(SetVariable):
    blockAction = "TrimList"

class SetVariable_SortList(SetVariable):
    blockAction = "SortList"

class SetVariable_ReverseList(SetVariable):
    blockAction = "ReverseList"

class SetVariable_RandomizeList(SetVariable):
    blockAction = "RandomizeList"

class SetVariable_FlattenList(SetVariable):
    blockAction = "FlattenList"

class SetVariable_ZipLists(SetVariable):
    blockAction = "ZipLists"

# Dictionary manipulation

class SetVariable_CreateDict(SetVariable):
    blockAction = "CreateDict"

class SetVariable_SetDictValue(SetVariable):
    blockAction = "SetDictValue"

class SetVariable_GetDictValue(SetVariable):
    blockAction = "GetDictValue"

class SetVariable_GetDictSize(SetVariable):
    blockAction = "GetDictSize"

class SetVariable_RemoveDictEntry(SetVariable):
    blockAction = "RemoveDictEntry"

class SetVariable_ClearDict(SetVariable):
    blockAction = "ClearDict"

class SetVariable_GetDictKeys(SetVariable):
    blockAction = "GetDictKeys"

class SetVariable_GetDictValues(SetVariable):
    blockAction = "GetDictValues"

class SetVariable_AppendDict(SetVariable):
    blockAction = "AppendDict"

class SetVariable_SortDict(SetVariable):
    blockAction = "SortDict"

# Particle manipulation

class SetVariable_GetParticleType(SetVariable):
    blockAction = "GetParticleType"

class SetVariable_SetParticleType(SetVariable):
    blockAction = "SetParticleType"

class SetVariable_GetParticleAmount(SetVariable):
    blockAction = "GetParticleAmount"

class SetVariable_SetParticleAmount(SetVariable):
    blockAction = "SetParticleAmount"

class SetVariable_GetParticleSprd(SetVariable):
    blockAction = "GetParticleSprd"

class SetVariable_SetParticleSprd(SetVariable):
    blockAction = "SetParticleSprd"

class SetVariable_GetParticleSize(SetVariable):
    blockAction = "GetParticleSize"

class SetVariable_SetParticleSize(SetVariable):
    blockAction = "SetParticleSize"

class SetVariable_GetParticleMat(SetVariable):
    blockAction = "GetParticleMat"

class SetVariable_SetParticleMat(SetVariable):
    blockAction = "SetParticleMat"

class SetVariable_GetParticleColor(SetVariable):
    blockAction = "GetParticleColor"

class SetVariable_SetParticleColor(SetVariable):
    blockAction = "SetParticleColor"

class SetVariable_GetParticleMotion(SetVariable):
    blockAction = "GetParticleMotion"

class SetVariable_SetParticleMotion(SetVariable):
    blockAction = "SetParticleMotion"

class SetVariable_GetParticleRoll(SetVariable):
    blockAction = "GetParticleRoll"

class SetVariable_SetParticleRoll(SetVariable):
    blockAction = "SetParticleRoll"

# World actions

class SetVariable_GetBlockType(SetVariable):
    blockAction = "GetBlockType"

class SetVariable_GetBlockData(SetVariable):
    blockAction = "GetBlockData"

class SetVariable_GetAllBlockData(SetVariable):
    blockAction = "GetAllBlockData"

class SetVariable_GetBlockGrowth(SetVariable):
    blockAction = "GetBlockGrowth"

class SetVariable_GetBlockPower(SetVariable):
    blockAction = "GetBlockPower"

class SetVariable_GetLight(SetVariable):
    blockAction = "GetLight"

class SetVariable_GetSignText(SetVariable):
    blockAction = "GetSignText"

class SetVariable_GetContainerName(SetVariable):
    blockAction = "GetContainerName"

class SetVariable_ContainerLock(SetVariable):
    blockAction = "ContainerLock"

class SetVariable_GetContainerItems(SetVariable):
    blockAction = "GetContainerItems"

class SetVariable_GetLecternBook(SetVariable):
    blockAction = "GetLecternBook"

class SetVariable_GetLecternPage(SetVariable):
    blockAction = "GetLecternPage"

class SetVariable_Raycast(SetVariable):
    blockAction = "Raycast"

# Miscellanious actions

class SetVariable_GetPotionType(SetVariable):
    blockAction = "GetPotionType"

class SetVariable_SetPotionType(SetVariable):
    blockAction = "SetPotionType"

class SetVariable_GetPotionAmp(SetVariable):
    blockAction = "GetPotionAmp"

class SetVariable_SetPotionAmp(SetVariable):
    blockAction = "SetPotionAmp"

class SetVariable_GetPotionDur(SetVariable):
    blockAction = "GetPotionDur"

class SetVariable_SetPotionDur(SetVariable):
    blockAction = "SetPotionDur"

class SetVariable_GetSoundType(SetVariable):
    blockAction = "GetSoundType"

class SetVariable_SetSoundType(SetVariable):
    blockAction = "SetSoundType"

class SetVariable_GetSoundVariant(SetVariable):
    blockAction = "GetSoundVariant"

class SetVariable_SetSoundVariant(SetVariable):
    blockAction = "SetSoundVariant"

class SetVariable_GetSoundPitch(SetVariable):
    blockAction = "GetSoundPitch"

class SetVariable_SetSoundPitch(SetVariable):
    blockAction = "SetSoundPitch"

class SetVariable_GetSoundVolume(SetVariable):
    blockAction = "GetSoundVolume"

class SetVariable_SetSoundVolume(SetVariable):
    blockAction = "SetSoundVolume"

class SetVariable_RGBColor(SetVariable):
    blockAction = "RGBColor"

class SetVariable_HSBColor(SetVariable):
    blockAction = "HSBColor"

class SetVariable_HSLColor(SetVariable):
    blockAction = "HSLColor"

class SetVariable_GetColorChannels(SetVariable):
    blockAction = "GetColorChannels"

# Vector manipulation

class SetVariable_Vector(SetVariable):
    blockAction = "Vector"

class SetVariable_VectorBetween(SetVariable):
    blockAction = "VectorBetween"

class SetVariable_GetVectorComp(SetVariable):
    blockAction = "GetVectorComp"

class SetVariable_SetVectorComp(SetVariable):
    blockAction = "SetVectorComp"

class SetVariable_GetVectorLength(SetVariable):
    blockAction = "GetVectorLength"

class SetVariable_SetVectorLength(SetVariable):
    blockAction = "SetVectorLength"

class SetVariable_MultiplyVector(SetVariable):
    blockAction = "MultiplyVector"

class SetVariable_AddVectors(SetVariable):
    blockAction = "AddVectors"

class SetVariable_SubtractVectors(SetVariable):
    blockAction = "SubtractVectors"

class SetVariable_AlignVector(SetVariable):
    blockAction = "AlignVector"

class SetVariable_RotateAroundAxis(SetVariable):
    blockAction = "RotateAroundAxis"

class SetVariable_RotateAroundVec(SetVariable):
    blockAction = "RotateAroundVec"

class SetVariable_ReflectVec(SetVariable):
    blockAction = "ReflectVec"

class SetVariable_CrossProduct(SetVariable):
    blockAction = "CrossProduct"

class SetVariable_DotProduct(SetVariable):
    blockAction = "DotProduct"

class SetVariable_DirectionName(SetVariable):
    blockAction = "DirectionName"

####################################
#             IF PLAYER            #
####################################

class IfPlayer(BaseBracketedBlock):
    blockType = "if_player"

# Toggleable conditions

class IfPlayer_IsSneaking(IfPlayer):
    blockAction = "IsSneaking"

class IfPlayer_IsSprinting(IfPlayer):
    blockAction = "IsSprinting"

class IfPlayer_IsGliding(IfPlayer):
    blockAction = "IsGliding"

class IfPlayer_IsFlying(IfPlayer):
    blockAction = "IsFlying"

class IfPlayer_IsGrounded(IfPlayer):
    blockAction = "IsGrounded"

class IfPlayer_IsSwimming(IfPlayer):
    blockAction = "IsSwimming"

class IfPlayer_IsBlocking(IfPlayer):
    blockAction = "IsBlocking"

# Locational conditions

class IfPlayer_IsLookingAt(IfPlayer):
    blockAction = "IsLookingAt"

class IfPlayer_StandingOn(IfPlayer):
    blockAction = "StandingOn"

class IfPlayer_IsNear(IfPlayer):
    blockAction = "IsNear"

class IfPlayer_InWorldBorder(IfPlayer):
    blockAction = "InWorldBorder"

# Item conditions

class IfPlayer_IsHolding(IfPlayer):
    blockAction = "IsHolding"

class IfPlayer_HasItem(IfPlayer):
    blockAction = "HasItem"

class IfPlayer_IsWearing(IfPlayer):
    blockAction = "IsWearing"

class IfPlayer_IsUsingItem(IfPlayer):
    blockAction = "IsUsingItem"

class IfPlayer_NoItemCooldown(IfPlayer):
    blockAction = "NoItemCooldown"

class IfPlayer_HasSlotItem(IfPlayer):
    blockAction = "HasSlotItem"

class IfPlayer_MenuSlotEquals(IfPlayer):
    blockAction = "MenuSlotEquals"

class IfPlayer_CursorItem(IfPlayer):
    blockAction = "CursorItem"

class IfPlayer_HasRoomForItem(IfPlayer):
    blockAction = "HasRoomForItem"

# Miscellanious conditions

class IfPlayer_NameEquals(IfPlayer):
    blockAction = "NameEquals"

class IfPlayer_SlotEquals(IfPlayer):
    blockAction = "SlotEquals"

class IfPlayer_HasPotion(IfPlayer):
    blockAction = "HasPotion"

class IfPlayer_IsRiding(IfPlayer):
    blockAction = "IsRiding"

class IfPlayer_InvOpen(IfPlayer):
    blockAction = "InvOpen"

class IfPlayer_HasPermission(IfPlayer):
    blockAction = "HasPermission"